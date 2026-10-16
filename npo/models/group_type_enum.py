from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "urn:vpro:media:2009"


class GroupTypeEnum(StrEnum):
    STRAND = "STRAND"
    ALBUM = "ALBUM"
    PLAYLIST = "PLAYLIST"
    ARCHIVE = "ARCHIVE"
    COLLECTION = "COLLECTION"
    SEASON = "SEASON"
    SERIES = "SERIES"
    UMBRELLA = "UMBRELLA"
