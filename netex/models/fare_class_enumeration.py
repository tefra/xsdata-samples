from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class FareClassEnumeration(Enum):
    UNKNOWN = "unknown"
    FIRST_CLASS = "firstClass"
    SECOND_CLASS = "secondClass"
    THIRD_CLASS = "thirdClass"
    PREFERENTE = "preferente"
    PREMIUM_CLASS = "premiumClass"
    BUSINESS_CLASS = "businessClass"
    STANDARD_CLASS = "standardClass"
    TURISTA = "turista"
    ECONOMY_CLASS = "economyClass"
    ANY = "any"
