from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


class TypeStayUnit(StrEnum):
    """
    Units for the Length of Stay.
    """

    MINUTES = "Minutes"
    HOURS = "Hours"
    DAYS = "Days"
    MONTHS = "Months"
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"
