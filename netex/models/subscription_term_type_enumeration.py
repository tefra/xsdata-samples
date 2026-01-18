from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SubscriptionTermTypeEnumeration(Enum):
    FIXED = "fixed"
    VARIABLE = "variable"
    OPEN_ENDED = "openEnded"
