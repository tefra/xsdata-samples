from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


class CabinType(Enum):
    """
    A cabin is either Premium First (P), First (F), Premium Business (J),
    Business (C), Premium Economy (S) or Economy (Y).
    """

    PREMIUM_FIRST = "PremiumFirst"
    FIRST = "First"
    PREMIUM_BUSINESS = "PremiumBusiness"
    BUSINESS = "Business"
    PREMIUM_ECONOMY = "PremiumEconomy"
    ECONOMY = "Economy"
    Y = "Y"
    S = "S"
    C = "C"
    J = "J"
    F = "F"
    P = "P"
