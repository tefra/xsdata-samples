from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from .alternative_texts_rel_structure import DataManagedObjectStructure
from .holiday_type_enumeration import HolidayTypeEnumeration
from .multilingual_string import MultilingualString
from .operating_day_ref_structure import OperatingDayRefStructure
from .season_enumeration import SeasonEnumeration
from .service_calendar_ref import ServiceCalendarRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OperatingPeriodVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "OperatingPeriod_VersionStructure"

    service_calendar_ref: Optional[ServiceCalendarRef] = field(
        default=None,
        metadata={
            "name": "ServiceCalendarRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    short_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    from_operating_day_ref: Optional[OperatingDayRefStructure] = field(
        default=None,
        metadata={
            "name": "FromOperatingDayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    from_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "FromDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    to_operating_day_ref: Optional[OperatingDayRefStructure] = field(
        default=None,
        metadata={
            "name": "ToOperatingDayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    to_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ToDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    holiday_type: List[HolidayTypeEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "HolidayType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    season: List[SeasonEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "Season",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 5,
        }
    )
