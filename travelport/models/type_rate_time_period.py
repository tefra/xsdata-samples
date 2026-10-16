from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


class TypeRateTimePeriod(StrEnum):
    """
    The period for the rate code (daily, weekly, etc).
    """

    HOURLY = "Hourly"
    DAILY = "Daily"
    WEEKLY = "Weekly"
    MONTHLY = "Monthly"
    WEEKEND_DAY = "WeekendDay"
    OTHER = "Other"
    PACKAGE = "Package"
    BUNDLE = "Bundle"
    TOTAL = "Total"
