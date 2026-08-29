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
    assert len(contacts) == 8
    assert not (repository_root / "assets" / "dzerba-2026-kontakty.vcf").exists()

    display_names: set[str] = set()
    for contact in contacts:
        path = repository_root / "assets" / "kontakty" / contact["filename"]
        raw = path.read_bytes()
        fields = properties(raw)

        assert fields["VERSION"] == ["3.0"]
        assert fields["N"] == [";;;;"]
        assert len(fields["FN"]) == 1
        assert len(fields["ORG"]) == 1
        assert len(fields["TEL"]) == 1
        assert unescape(fields["FN"][0]) == contact["display_name"]
        assert unescape(fields["ORG"][0]) == contact["display_name"]
        assert fields["TEL"][0] == contact["phone"]
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

    page_text = (repository_root / "praktyczne.md").read_text(encoding="utf-8")
    links = re.findall(r"\]\(([^)]+\.vcf)\)", page_text)
    labels = re.findall(r"\[([^]]+)\]\([^)]+\.vcf\)", page_text)
    expected_links = [f"assets/kontakty/{contact['filename']}" for contact in contacts]
    expected_labels = [f"Pobierz kontakt: {contact['display_name']}" for contact in contacts]
    assert links == expected_links
    assert labels == expected_labels
    assert len(set(links)) == len(set(labels)) == 8
    assert all((repository_root / link).is_file() for link in links)
    print(f"OK: {len(contacts)} individual vCard files")
    print("OK: 8 existing targets with exact, unique descriptive link labels")


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
