from dataclasses import dataclass, field
from typing import List, Optional, Union
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
    from_operating_day_ref_or_from_date: Optional[Union[OperatingDayRefStructure, XmlDateTime]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FromOperatingDayRef",
                    "type": OperatingDayRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FromDate",
                    "type": XmlDateTime,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    to_operating_day_ref_or_to_date: Optional[Union[OperatingDayRefStructure, XmlDateTime]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ToOperatingDayRef",
                    "type": OperatingDayRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ToDate",
                    "type": XmlDateTime,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
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
