from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class RoutingTypeEnumeration(Enum):
    DIRECT = "direct"
    INDIRECT = "indirect"
    BOTH = "both"
