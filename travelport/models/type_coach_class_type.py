from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/rail_v52_0"


class TypeCoachClassType(Enum):
    """
    Values for accommodation class.
    """

    FIRST_CLASS = "First Class"
    STANDARD_CLASS = "Standard Class"
    FIRST_AND_STANDARD_CLASS = "First and Standard Class"
    OTHER = "Other"
