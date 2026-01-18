from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class PublicHolidayTypeEnum(Enum):
    """
    Types of public holiday.

    :cvar BETWEEN_CHRISTMAS_AND_NEW_YEAR: The days between the Christmas
        and New Year public holidays which are not official public
        holidays.
    :cvar BOXING_DAY: The day following Christmas day.
    :cvar BRIDGE_HOLIDAY: A day between a public holiday and the
        weekend.
    :cvar CHRISTMAS_EVE: The day before Christmas day.
    :cvar CHRISTMAS_DAY_AND_BOXING_DAY: Christmas day and Boxing day
        (day following Christmas day).
    :cvar CHRISTMAS_HOLIDAY_PERIOD: The period between the Christmas and
        New Year public holidays (inclusive).
    :cvar DAY_FOLLOWING_PUBLIC_HOLIDAY: A day following a public
        holiday.
    :cvar EASTER_FRIDAY_HOLIDAY: Good Friday (the Friday prior to the
        Easter weekend).
    :cvar EASTER_HOLIDAY_PERIOD: The period between Easter Friday and
        Easter Monday (inclusive).
    :cvar EASTER_MONDAY_HOLIDAY: The Monday following the Easter
        weekend.
    :cvar EASTER_SATURDAY: The Saturday of the Easter weekend.
    :cvar EASTER_SUNDAY: Easter Sunday.
    :cvar EVE_OF_PUBLIC_HOLIDAY: The day preceding a public holiday.
    :cvar HOLIDAY_PERIOD: A holiday period.
    :cvar IN_LIEU_OF_PUBLIC_HOLIDAY: A holiday in lieu of a public
        holiday that falls on a weekend.
    :cvar JANUARY2ND_HOLIDAY: The 2nd of January holiday.
    :cvar NEW_YEARS_DAY: New Year's day.
    :cvar NEW_YEARS_EVE: The day before New Year's day.
    :cvar NOT_PUBLIC_HOLIDAY: A day that is not a public holiday.
    :cvar PUBLIC_HOLIDAY: A public holiday in the respective
        country/region.
    :cvar OTHER: None of the elements in the list. Public holiday is
        specified by 'publicHolidayName' instead.
    """

    BETWEEN_CHRISTMAS_AND_NEW_YEAR = "betweenChristmasAndNewYear"
    BOXING_DAY = "boxingDay"
    BRIDGE_HOLIDAY = "bridgeHoliday"
    CHRISTMAS_EVE = "christmasEve"
    CHRISTMAS_DAY_AND_BOXING_DAY = "christmasDayAndBoxingDay"
    CHRISTMAS_HOLIDAY_PERIOD = "christmasHolidayPeriod"
    DAY_FOLLOWING_PUBLIC_HOLIDAY = "dayFollowingPublicHoliday"
    EASTER_FRIDAY_HOLIDAY = "easterFridayHoliday"
    EASTER_HOLIDAY_PERIOD = "easterHolidayPeriod"
    EASTER_MONDAY_HOLIDAY = "easterMondayHoliday"
    EASTER_SATURDAY = "easterSaturday"
    EASTER_SUNDAY = "easterSunday"
    EVE_OF_PUBLIC_HOLIDAY = "eveOfPublicHoliday"
    HOLIDAY_PERIOD = "holidayPeriod"
    IN_LIEU_OF_PUBLIC_HOLIDAY = "inLieuOfPublicHoliday"
    JANUARY2ND_HOLIDAY = "january2ndHoliday"
    NEW_YEARS_DAY = "newYearsDay"
    NEW_YEARS_EVE = "newYearsEve"
    NOT_PUBLIC_HOLIDAY = "notPublicHoliday"
    PUBLIC_HOLIDAY = "publicHoliday"
    OTHER = "other"
