from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


class UrticketStatus(Enum):
    """
    Information on whether the Universal Record ticket status is Ticketed,
    Unticketed , Partially Ticketed or Not Applicable status.
    """

    TICKETED = "Ticketed"
    UNTICKETED = "Unticketed"
    PARTIALLY_TICKETED = "Partially Ticketed"
    NOT_APPLICABLE = "Not Applicable"
