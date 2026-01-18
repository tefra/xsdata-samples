from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class WeekOfMonthEnum(Enum):
    """
    Weeks of the month.

    :cvar FIRST_WEEK_OF_MONTH: First week of the month.
    :cvar SECOND_WEEK_OF_MONTH: Second week of the month.
    :cvar THIRD_WEEK_OF_MONTH: Third week of the month.
    :cvar FOURTH_WEEK_OF_MONTH: Fourth week of the month.
    :cvar FIFTH_WEEK_OF_MONTH: Fifth week of the month (at most only 3
        days and non in February when not a leap year).
    """

    FIRST_WEEK_OF_MONTH = "firstWeekOfMonth"
    SECOND_WEEK_OF_MONTH = "secondWeekOfMonth"
    THIRD_WEEK_OF_MONTH = "thirdWeekOfMonth"
    FOURTH_WEEK_OF_MONTH = "fourthWeekOfMonth"
    FIFTH_WEEK_OF_MONTH = "fifthWeekOfMonth"
