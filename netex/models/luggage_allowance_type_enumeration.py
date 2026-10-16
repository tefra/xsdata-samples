from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class LuggageAllowanceTypeEnumeration(StrEnum):
    NONE = "none"
    SINGLE_BAG = "singleBag"
    LIMITED = "limited"
    UNLIMITED = "unlimited"
