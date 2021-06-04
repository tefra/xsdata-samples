from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class VersionStatusEnumeration(Enum):
    DRAFT = "draft"
    VERSIONED = "versioned"
    DEPRECATED = "deprecated"
    OTHER = "other"
