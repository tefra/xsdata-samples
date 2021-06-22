from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class VersionStatusEnumeration(Enum):
    DRAFT = "draft"
    PROPOSED = "proposed"
    VERSIONED = "versioned"
    DEPRECATED = "deprecated"
    OTHER = "other"
