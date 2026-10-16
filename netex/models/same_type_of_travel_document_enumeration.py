from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SameTypeOfTravelDocumentEnumeration(StrEnum):
    ANY = "any"
    SAME = "same"
    SAME_MEDIA = "sameMedia"
    SAME_SMARTCARD = "sameSmartcard"
    SAME_MOBILE_APP = "sameMobileApp"
    DIFFERENT = "different"
