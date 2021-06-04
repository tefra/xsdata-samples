from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ContainmentEnumeration(Enum):
    INLINE = "inline"
    BY_REFERENCE = "byReference"
    BY_VERSIONED_REFERENCE = "byVersionedReference"
    BOTH = "both"
