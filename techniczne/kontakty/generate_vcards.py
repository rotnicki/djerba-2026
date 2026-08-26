#!/usr/bin/env python3
"""Generate conservative vCard 3.0 files for the Djerba 2026 guide."""

from __future__ import annotations

import argparse
from pathlib import Path

import yaml


CRLF = "\r\n"
MAX_OCTETS = 75


def escape_text(value: str) -> str:
    return (
        value.replace("\\", "\\\\")
        .replace("\n", "\\n")
        .replace(";", "\\;")
        .replace(",", "\\,")
    )


def fold_line(line: str) -> list[str]:
    """Fold a logical content line without splitting UTF-8 characters."""
    physical: list[str] = []
    current = ""
    limit = MAX_OCTETS

    for character in line:
        encoded_length = len(character.encode("utf-8"))
        if current and len(current.encode("utf-8")) + encoded_length > limit:
            physical.append(current)
            current = " " + character
            limit = MAX_OCTETS
        else:
            current += character

    physical.append(current)
    return physical


def content_line(name: str, value: str, parameters: str | None = None) -> list[str]:
    key = name if not parameters else f"{name};{parameters}"
    return fold_line(f"{key}:{value}")


def address_value(address: dict[str, str]) -> str:
    components = [
        address.get("po_box", ""),
        address.get("extended", ""),
        address.get("street", ""),
        address.get("locality", ""),
        address.get("region", ""),
        address.get("postal_code", ""),
        address.get("country", ""),
    ]
    return ";".join(escape_text(component) for component in components)


def render_card(contact: dict[str, object]) -> bytes:
    lines = ["BEGIN:VCARD", "VERSION:3.0", "N:;;;;"]
    lines += content_line("FN", escape_text(str(contact["display_name"])))
    # iOS displays ORG instead of FN when N is empty.  Use the same concise,
    # searchable label in both fields so institutions remain distinguishable.
    lines += content_line("ORG", escape_text(str(contact["display_name"])))

    phone_parameters = None
    if contact.get("phone_type"):
        phone_parameters = f"TYPE={contact['phone_type']}"
    lines += content_line("TEL", str(contact["phone"]), phone_parameters)

    if contact.get("email"):
        lines += content_line("EMAIL", str(contact["email"]), "TYPE=INTERNET")
    if contact.get("address"):
        lines += content_line(
            "ADR", address_value(contact["address"]), "TYPE=WORK"
        )
    if contact.get("note"):
        lines += content_line("NOTE", escape_text(str(contact["note"])))

    lines.append("END:VCARD")
    return (CRLF.join(lines) + CRLF).encode("utf-8")


def generate(source: Path, repository_root: Path) -> None:
    data = yaml.safe_load(source.read_text(encoding="utf-8"))
    contacts = data["contacts"]
    output_directory = repository_root / "assets" / "kontakty"
    output_directory.mkdir(parents=True, exist_ok=True)

    cards: list[bytes] = []
    for contact in contacts:
        card = render_card(contact)
        cards.append(card)
        (output_directory / contact["filename"]).write_bytes(card)

    (repository_root / "assets" / "dzerba-2026-kontakty.vcf").write_bytes(
        b"".join(cards)
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source",
        type=Path,
        default=Path(__file__).with_name("kontakty.yml"),
    )
    parser.add_argument(
        "--repository-root",
        type=Path,
        default=Path(__file__).resolve().parents[2],
    )
    arguments = parser.parse_args()
    generate(arguments.source, arguments.repository_root)


if __name__ == "__main__":
    main()
