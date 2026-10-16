from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ContainmentEnumeration(StrEnum):
    INLINE = "inline"
    BY_REFERENCE = "byReference"
    BY_VERSIONED_REFERENCE = "byVersionedReference"
    BOTH = "both"
