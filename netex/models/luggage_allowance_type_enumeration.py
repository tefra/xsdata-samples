from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class LuggageAllowanceTypeEnumeration(Enum):
    NONE = "none"
    SINGLE_BAG = "singleBag"
    LIMITED = "limited"
    UNLIMITED = "unlimited"
