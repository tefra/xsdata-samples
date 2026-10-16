from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class MarkedAsEnumeration(StrEnum):
    UNUSED = "unused"
    ACTIVATED = "activated"
    MARKED = "marked"
    USED = "used"
    EXPIRED = "expired"
