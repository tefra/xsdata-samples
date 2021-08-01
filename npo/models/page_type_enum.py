from enum import Enum

__NAMESPACE__ = "urn:vpro:pages:2013"


class PageTypeEnum(Enum):
    ARTICLE = "ARTICLE"
    SPECIAL = "SPECIAL"
    HOME = "HOME"
    OVERVIEW = "OVERVIEW"
    PRODUCT = "PRODUCT"
    PLAYER = "PLAYER"
    AUDIO = "AUDIO"
    VIDEO = "VIDEO"
    MIXED = "MIXED"
    PLAYLIST = "PLAYLIST"
    MOVIE = "MOVIE"
    SERIES = "SERIES"
    PERSON = "PERSON"
    SEARCH = "SEARCH"
