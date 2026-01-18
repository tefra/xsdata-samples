from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

from datexii.models.eu.datexii.v2.day_week_month import DayWeekMonth
from datexii.models.eu.datexii.v2.multilingual_string import MultilingualString
from datexii.models.eu.datexii.v2.period_extension_type import (
    PeriodExtensionType,
)
from datexii.models.eu.datexii.v2.time_period_of_day import TimePeriodOfDay

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class Period:
    """
    A continuous time period or a set of discontinuous time periods defined
    by the intersection of a set of criteria all within an overall
    delimiting interval.

    :ivar start_of_period: Start of period.
    :ivar end_of_period: End of a period.
    :ivar period_name: The name of the period.
    :ivar recurring_time_period_of_day: A recurring period of a day.
    :ivar recurring_day_week_month_period: A recurring period defined in
        terms of days of the week, weeks of the month and months of the
        year.
    :ivar period_extension:
    """

    start_of_period: XmlDateTime | None = field(
        default=None,
        metadata={
            "name": "startOfPeriod",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    end_of_period: XmlDateTime | None = field(
        default=None,
        metadata={
            "name": "endOfPeriod",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    period_name: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "periodName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    recurring_time_period_of_day: list[TimePeriodOfDay] = field(
        default_factory=list,
        metadata={
            "name": "recurringTimePeriodOfDay",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    recurring_day_week_month_period: list[DayWeekMonth] = field(
        default_factory=list,
        metadata={
            "name": "recurringDayWeekMonthPeriod",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    period_extension: PeriodExtensionType | None = field(
        default=None,
        metadata={
            "name": "periodExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
