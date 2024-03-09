from dataclasses import dataclass, field
from typing import List, Optional

from datexii.models.eu.datexii.v2.day_enum import DayEnum
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.month_of_year_enum import MonthOfYearEnum
from datexii.models.eu.datexii.v2.week_of_month_enum import WeekOfMonthEnum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class DayWeekMonth:
    """
    Specification of periods defined by the intersection of days, weeks and months.

    :ivar applicable_day: Applicable day of the week. "All days of the
        week" is expressed by non-inclusion of this attribute.
    :ivar applicable_week: Applicable week of the month (1 to 5).  "All
        weeks of the month" is expressed by non-inclusion of this
        attribute.
    :ivar applicable_month: Applicable month of the year.  "All months
        of the year" is expressed by non-inclusion of this attribute.
    :ivar day_week_month_extension:
    """

    applicable_day: List[DayEnum] = field(
        default_factory=list,
        metadata={
            "name": "applicableDay",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_occurs": 7,
        },
    )
    applicable_week: List[WeekOfMonthEnum] = field(
        default_factory=list,
        metadata={
            "name": "applicableWeek",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_occurs": 5,
        },
    )
    applicable_month: List[MonthOfYearEnum] = field(
        default_factory=list,
        metadata={
            "name": "applicableMonth",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_occurs": 12,
        },
    )
    day_week_month_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "dayWeekMonthExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
