from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


class TypePurposeCode(Enum):
    """
    List of valid Purpose Codes.

    Properties
    ----------
    BUSINESS
        Business
    PLEASURE
        Pleasure
    CHARTER_SERVICE
        Charter Service
    """

    BUSINESS = "Business"
    PLEASURE = "Pleasure"
    CHARTER_SERVICE = "CharterService"
