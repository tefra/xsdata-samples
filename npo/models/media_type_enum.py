from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "urn:vpro:media:2009"


class MediaTypeEnum(Enum):
    MEDIA = "MEDIA"
    GROUP = "GROUP"
    PROGRAM = "PROGRAM"
    SEGMENTTYPE = "SEGMENTTYPE"
    STRAND = "STRAND"
    ALBUM = "ALBUM"
    PLAYLIST = "PLAYLIST"
    ARCHIVE = "ARCHIVE"
    SEASON = "SEASON"
    SERIES = "SERIES"
    UMBRELLA = "UMBRELLA"
    BROADCAST = "BROADCAST"
    MOVIE = "MOVIE"
    TRAILER = "TRAILER"
    CLIP = "CLIP"
    TRACK = "TRACK"
    SEGMENT = "SEGMENT"
    VISUALRADIO = "VISUALRADIO"
    VISUALRADIOSEGMENT = "VISUALRADIOSEGMENT"
    PROMO = "PROMO"
    RECORDING = "RECORDING"
    COLLECTION = "COLLECTION"


MediaTypeEnum.MEDIA.__doc__ = (
    "The abstract type denoting every possible media type"
)
MediaTypeEnum.GROUP.__doc__ = (
    "The abstract type denoting every possible group type"
)
MediaTypeEnum.PROGRAM.__doc__ = (
    "The abstract type denoting every possible program type"
)
MediaTypeEnum.SEGMENTTYPE.__doc__ = (
    "The abstract type denoting every possible segment type"
)
