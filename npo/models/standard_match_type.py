from enum import Enum

__NAMESPACE__ = "urn:vpro:api:2013"


class StandardMatchType(Enum):
    TEXT = "TEXT"
    REGEX = "REGEX"
    WILDCARD = "WILDCARD"
