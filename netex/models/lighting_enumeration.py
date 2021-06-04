from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class LightingEnumeration(Enum):
    WELL_LIT = "wellLit"
    POORLY_LIT = "poorlyLit"
    UNLIT = "unlit"
    UNKNOWN = "unknown"
    OTHER = "other"
