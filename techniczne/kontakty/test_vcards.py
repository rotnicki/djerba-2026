#!/usr/bin/env python3
"""Automated structural and semantic tests for generated vCards."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml


def unfold(raw: bytes) -> list[str]:
    if b"\n" in raw.replace(b"\r\n", b""):
        raise AssertionError("A file contains an LF not preceded by CR")
    if b"\r" in raw.replace(b"\r\n", b""):
        raise AssertionError("A file contains a CR not followed by LF")

    physical = raw.decode("utf-8").split("\r\n")
    assert physical[-1] == "", "The file must end with CRLF"
    physical.pop()

    for line in physical:
        assert len(line.encode("utf-8")) <= 75, (
            f"Physical line exceeds 75 octets: {line!r}"
        )

    logical: list[str] = []
    for line in physical:
        if line.startswith((" ", "\t")):
            assert logical, "Continuation cannot be the first line"
            logical[-1] += line[1:]
        else:
            logical.append(line)
    return logical


def split_cards(raw: bytes) -> list[bytes]:
    marker = b"END:VCARD\r\n"
    chunks = raw.split(marker)
    assert chunks[-1] == b"", "Unexpected data after final vCard"
    return [chunk + marker for chunk in chunks[:-1]]


def unescape(value: str) -> str:
    return re.sub(
        r"\\([\\,;nN])",
        lambda match: "\n" if match.group(1).lower() == "n" else match.group(1),
        value,
    )


def properties(card: bytes) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for line in unfold(card):
        if line in {"BEGIN:VCARD", "END:VCARD"}:
            continue
        key, separator, value = line.partition(":")
        assert separator, f"Content line without colon: {line!r}"
        base_name = key.split(";", 1)[0].upper()
        result.setdefault(base_name, []).append(value)
    return result


def test(repository_root: Path, source: Path) -> None:
    data = yaml.safe_load(source.read_text(encoding="utf-8"))
    contacts = data["contacts"]
    aggregate_path = repository_root / "assets" / "dzerba-2026-kontakty.vcf"
    aggregate = aggregate_path.read_bytes()
    aggregate_cards = split_cards(aggregate)
    assert len(aggregate_cards) == len(contacts) == 8

    expected_aggregate = b""
    display_names: set[str] = set()
    for index, contact in enumerate(contacts):
        path = repository_root / "assets" / "kontakty" / contact["filename"]
        raw = path.read_bytes()
        expected_aggregate += raw
        assert split_cards(raw) == [raw]
        fields = properties(raw)

        assert fields["VERSION"] == ["3.0"]
        assert fields["N"] == [";;;;"]
        assert len(fields["FN"]) == 1
        assert len(fields["ORG"]) == 1
        assert len(fields["TEL"]) == 1
        assert unescape(fields["FN"][0]) == contact["display_name"]
        assert unescape(fields["ORG"][0]) == contact["display_name"]
        assert fields["TEL"][0] == contact["phone"]
        assert aggregate_cards[index] == raw
        assert contact["display_name"].startswith(data["prefix"])
        assert contact["display_name"] not in display_names
        display_names.add(contact["display_name"])
        assert fields["FN"] == fields["ORG"]

        if contact.get("email"):
            assert fields["EMAIL"] == [contact["email"]]
        else:
            assert "EMAIL" not in fields
        if contact.get("address"):
            assert len(fields["ADR"]) == 1
        else:
            assert "ADR" not in fields
        if contact.get("note"):
            assert unescape(fields["NOTE"][0]) == contact["note"]

    assert aggregate == expected_aggregate

    test_page = repository_root / "test-kontakty-vcard.md"
    page_text = test_page.read_text(encoding="utf-8")
    links = re.findall(r"\]\(([^)]+\.vcf)\)", page_text)
    labels = re.findall(r"\[([^]]+)\]\([^)]+\.vcf\)", page_text)
    assert len(links) == len(labels) == 9
    assert len(set(links)) == len(set(labels)) == 9
    assert all((repository_root / link).is_file() for link in links)
    assert all(label.startswith("Pobierz ") for label in labels)
    print(f"OK: {len(contacts)} individual cards and one aggregate card file")
    print("OK: 9 existing targets with unique descriptive link labels")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("repository_root", type=Path)
    parser.add_argument("source", type=Path)
    arguments = parser.parse_args()
    try:
        test(arguments.repository_root, arguments.source)
    except (AssertionError, KeyError, UnicodeDecodeError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        raise SystemExit(1) from error


if __name__ == "__main__":
    main()
