from enum import Enum

__NAMESPACE__ = "urn:vpro:media:2009"


class GroupTypeEnum(Enum):
    STRAND = "STRAND"
    ALBUM = "ALBUM"
    PLAYLIST = "PLAYLIST"
    ARCHIVE = "ARCHIVE"
    COLLECTION = "COLLECTION"
    SEASON = "SEASON"
    SERIES = "SERIES"
    UMBRELLA = "UMBRELLA"
