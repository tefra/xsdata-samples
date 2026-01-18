from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import ForwardRef, Optional, Union

from xsdata.models.datatype import XmlPeriod

from .country_ref_structure import CountryRefStructure
from .crowding_enumeration import CrowdingEnumeration
from .day_event_enumeration import DayEventEnumeration
from .day_of_week_enumeration import DayOfWeekEnumeration
from .holiday_type_enumeration import HolidayTypeEnumeration
from .multilingual_string import MultilingualString
from .season_enumeration import SeasonEnumeration
from .tide_enumeration import TideEnumeration
from .week_of_month_enumeration import WeekOfMonthEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PropertyOfDayStructure:
    name: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    days_of_week: Iterable[DayOfWeekEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "DaysOfWeek",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    weeks_of_month: Iterable[WeekOfMonthEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "WeeksOfMonth",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    month_of_year_or_day_of_month_or_day_of_year: PropertyOfDayStructure.MonthOfYear | PropertyOfDayStructure.DayOfMonth | PropertyOfDayStructure.DayOfYear | None = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "MonthOfYear",
                    "type": ForwardRef("PropertyOfDayStructure.MonthOfYear"),
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DayOfMonth",
                    "type": ForwardRef("PropertyOfDayStructure.DayOfMonth"),
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DayOfYear",
                    "type": ForwardRef("PropertyOfDayStructure.DayOfYear"),
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    country_ref: CountryRefStructure | None = field(
        default=None,
        metadata={
            "name": "CountryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    holiday_types: Iterable[HolidayTypeEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "HolidayTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    seasons: Iterable[SeasonEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "Seasons",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    tides: Iterable[TideEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "Tides",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    day_event: DayEventEnumeration | None = field(
        default=None,
        metadata={
            "name": "DayEvent",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    crowding: CrowdingEnumeration | None = field(
        default=None,
        metadata={
            "name": "Crowding",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )

    @dataclass
    class MonthOfYear:
        value: XmlPeriod | None = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class DayOfMonth:
        value: XmlPeriod | None = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass
    class DayOfYear:
        value: XmlPeriod | None = field(
            default=None,
            metadata={
                "required": True,
            },
        )
