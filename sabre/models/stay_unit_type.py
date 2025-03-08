from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


class StayUnitType(Enum):
    """
    Defines the 'Units' that can be applied to Stay restrictions.

    Attributes:
        MINUTES:
        HOURS:
        DAYS:
        MONTHS:
        MON: Monday
        TUES: Tuesday
        WED: Wednesday
        THU: Thursday
        FRI: Friday
        SAT: Saturday
        SUN: Sunday
    """

    MINUTES = "Minutes"
    HOURS = "Hours"
    DAYS = "Days"
    MONTHS = "Months"
    MON = "MON"
    TUES = "TUES"
    WED = "WED"
    THU = "THU"
    FRI = "FRI"
    SAT = "SAT"
    SUN = "SUN"
