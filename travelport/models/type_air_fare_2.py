from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


class TypeAirFare2(StrEnum):
    """
    The type of Air Fare.
    """

    ADVANCE_PURCHASE_FARES = "Advance Purchase Fares"
    NON_REFUNDABLE_FARES = "Non-Refundable Fares"
    PENALTY_FARES = "Penalty Fares"
    PRIVATE_FARES_ONLY = "Private Fares Only"
    RESTRICTED_FARES = "Restricted Fares"
