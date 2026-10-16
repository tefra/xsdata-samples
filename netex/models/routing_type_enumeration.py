from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class RoutingTypeEnumeration(StrEnum):
    DIRECT = "direct"
    INDIRECT = "indirect"
    BOTH = "both"
