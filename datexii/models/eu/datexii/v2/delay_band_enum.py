from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class DelayBandEnum(Enum):
    """
    Classifications of a delay banded by length (i.e. the additional travel
    time).

    :cvar NEGLIGIBLE: Negligible delay.
    :cvar UP_TO_TEN_MINUTES: Delay up to ten minutes.
    :cvar BETWEEN_TEN_MINUTES_AND_THIRTY_MINUTES: Delay between ten
        minutes and thirty minutes.
    :cvar BETWEEN_THIRTY_MINUTES_AND_ONE_HOUR: Delay between thirty
        minutes and one hour.
    :cvar BETWEEN_ONE_HOUR_AND_THREE_HOURS: Delay between one hour and
        three hours.
    :cvar BETWEEN_THREE_HOURS_AND_SIX_HOURS: Delay between three hours
        and six hours.
    :cvar LONGER_THAN_SIX_HOURS: Delay longer than six hours.
    """

    NEGLIGIBLE = "negligible"
    UP_TO_TEN_MINUTES = "upToTenMinutes"
    BETWEEN_TEN_MINUTES_AND_THIRTY_MINUTES = (
        "betweenTenMinutesAndThirtyMinutes"
    )
    BETWEEN_THIRTY_MINUTES_AND_ONE_HOUR = "betweenThirtyMinutesAndOneHour"
    BETWEEN_ONE_HOUR_AND_THREE_HOURS = "betweenOneHourAndThreeHours"
    BETWEEN_THREE_HOURS_AND_SIX_HOURS = "betweenThreeHoursAndSixHours"
    LONGER_THAN_SIX_HOURS = "longerThanSixHours"
