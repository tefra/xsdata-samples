from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "urn:vpro:media:2009"


class TextualTypeEnum(StrEnum):
    MAIN = "MAIN"
    SHORT = "SHORT"
    SUB = "SUB"
    KICKER = "KICKER"
    ORIGINAL = "ORIGINAL"
    EPISODE = "EPISODE"
    WORK = "WORK"
    LEXICO = "LEXICO"
    ABBREVIATION = "ABBREVIATION"
