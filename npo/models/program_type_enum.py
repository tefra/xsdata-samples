from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "urn:vpro:media:2009"


class ProgramTypeEnum(StrEnum):
    BROADCAST = "BROADCAST"
    MOVIE = "MOVIE"
    TRAILER = "TRAILER"
    CLIP = "CLIP"
    STRAND = "STRAND"
    TRACK = "TRACK"
    VISUALRADIO = "VISUALRADIO"
    PROMO = "PROMO"
    RECORDING = "RECORDING"
