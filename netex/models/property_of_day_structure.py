from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlPeriod
from netex.models.country_ref_structure import CountryRefStructure
from netex.models.crowding_enumeration import CrowdingEnumeration
from netex.models.day_event_enumeration import DayEventEnumeration
from netex.models.day_of_week_enumeration import DayOfWeekEnumeration
from netex.models.holiday_type_enumeration import HolidayTypeEnumeration
from netex.models.multilingual_string import MultilingualString
from netex.models.season_enumeration import SeasonEnumeration
from netex.models.tide_enumeration import TideEnumeration
from netex.models.week_of_month_enumeration import WeekOfMonthEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PropertyOfDayStructure:
    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    days_of_week: List[DayOfWeekEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "DaysOfWeek",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    weeks_of_month: List[WeekOfMonthEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "WeeksOfMonth",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    month_of_year: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "MonthOfYear",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    day_of_month: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "DayOfMonth",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    day_of_year: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "DayOfYear",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    country_ref: Optional[CountryRefStructure] = field(
        default=None,
        metadata={
            "name": "CountryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    holiday_types: List[HolidayTypeEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "HolidayTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    seasons: List[SeasonEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "Seasons",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    tides: List[TideEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "Tides",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    day_event: Optional[DayEventEnumeration] = field(
        default=None,
        metadata={
            "name": "DayEvent",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    crowding: Optional[CrowdingEnumeration] = field(
        default=None,
        metadata={
            "name": "Crowding",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
