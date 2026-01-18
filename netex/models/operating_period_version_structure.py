from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

from .entity_in_version_structure import DataManagedObjectStructure
from .holiday_type_enumeration import HolidayTypeEnumeration
from .multilingual_string import MultilingualString
from .operating_day_ref_structure import OperatingDayRefStructure
from .season_enumeration import SeasonEnumeration
from .service_calendar_ref import ServiceCalendarRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OperatingPeriodVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "OperatingPeriod_VersionStructure"

    service_calendar_ref: None | ServiceCalendarRef = field(
        default=None,
        metadata={
            "name": "ServiceCalendarRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    name: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    short_name: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    from_operating_day_ref_or_from_date: (
        None | OperatingDayRefStructure | XmlDateTime
    ) = field(
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
        },
    )
    to_operating_day_ref_or_to_date: (
        None | OperatingDayRefStructure | XmlDateTime
    ) = field(
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
        },
    )
    holiday_type: Iterable[HolidayTypeEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "HolidayType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    season: Iterable[SeasonEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "Season",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 5,
        },
    )
