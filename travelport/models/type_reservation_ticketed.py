from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


class TypeReservationTicketed(StrEnum):
    """
    Information on whether the reservation is ticketed.
    """

    YES = "Yes"
    NO = "No"
    NOT_APPLICABLE = "Not Applicable"
