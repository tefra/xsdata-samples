from enum import Enum

__NAMESPACE__ = "urn:vpro:media:2009"


class ProgramTypeEnum(Enum):
    BROADCAST = "BROADCAST"
    MOVIE = "MOVIE"
    TRAILER = "TRAILER"
    CLIP = "CLIP"
    STRAND = "STRAND"
    TRACK = "TRACK"
    VISUALRADIO = "VISUALRADIO"
    PROMO = "PROMO"
    RECORDING = "RECORDING"
