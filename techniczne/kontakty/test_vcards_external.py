#!/usr/bin/env python3
"""Round-trip tests using two external vCard parsers."""

from __future__ import annotations

import argparse
from pathlib import Path

import vobject
import vobjectx


def read_text(path: Path) -> str:
    with path.open("r", encoding="utf-8", newline="") as file:
        return file.read()


def test_with_vobject(path: Path, expected_count: int) -> None:
    cards = list(vobject.readComponents(read_text(path), validate=True))
    assert len(cards) == expected_count
    for card in cards:
        assert card.version.value == "3.0"
        assert card.fn.value.startswith("Djerba —")
        assert card.org.value
        assert card.tel.value
        serialized = card.serialize(validate=True)
        reread = list(vobject.readComponents(serialized, validate=True))
        assert len(reread) == 1
        assert reread[0].fn.value == card.fn.value
        assert reread[0].org.value == card.org.value
        assert reread[0].tel.value == card.tel.value


def test_with_vobjectx(path: Path, expected_count: int) -> None:
    # vobjectx 0.6.1 emits one additional unnamed empty component for a
    # trailing CRLF. Only named VCARD components are relevant here.
    cards = [
        component
        for component in vobjectx.read_components(read_text(path), validate=True)
        if component.name == "VCARD"
    ]
    assert len(cards) == expected_count
    for card in cards:
        assert card.version.value == "3.0"
        assert card.fn.value.startswith("Djerba —")
        assert card.org.value
        assert card.tel.value
        serialized = card.serialize(validate=True)
        reread = [
            component
            for component in vobjectx.read_components(serialized, validate=True)
            if component.name == "VCARD"
        ]
        assert len(reread) == 1
        assert reread[0].fn.value == card.fn.value
        assert reread[0].org.value == card.org.value
        assert reread[0].tel.value == card.tel.value


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("repository_root", type=Path)
    arguments = parser.parse_args()

    paths = sorted((arguments.repository_root / "assets").rglob("*.vcf"))
    assert len(paths) == 9
    for path in paths:
        expected_count = 8 if path.name == "dzerba-2026-kontakty.vcf" else 1
        test_with_vobject(path, expected_count)
        test_with_vobjectx(path, expected_count)
        print(f"OK: {path} ({expected_count} vCard)")


if __name__ == "__main__":
    main()
