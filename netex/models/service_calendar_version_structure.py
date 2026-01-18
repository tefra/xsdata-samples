from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate, XmlDuration, XmlTime

from .day_type_assignments_rel_structure import DayTypeAssignmentsRelStructure
from .entity_in_version_structure import (
    DataManagedObjectStructure,
    DayTypesRelStructure,
    OperatingDaysRelStructure,
    TimebandsRelStructure,
)
from .multilingual_string import MultilingualString
from .operating_periods_rel_structure import OperatingPeriodsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ServiceCalendarVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "ServiceCalendar_VersionStructure"

    name: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    short_name: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    from_date: XmlDate | None = field(
        default=None,
        metadata={
            "name": "FromDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    to_date: XmlDate | None = field(
        default=None,
        metadata={
            "name": "ToDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    earliest_time: XmlTime | None = field(
        default=None,
        metadata={
            "name": "EarliestTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    day_length: XmlDuration | None = field(
        default=None,
        metadata={
            "name": "DayLength",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    day_types: DayTypesRelStructure | None = field(
        default=None,
        metadata={
            "name": "dayTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    timebands: TimebandsRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    operating_days: OperatingDaysRelStructure | None = field(
        default=None,
        metadata={
            "name": "operatingDays",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    operating_periods: OperatingPeriodsRelStructure | None = field(
        default=None,
        metadata={
            "name": "operatingPeriods",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    day_type_assignments: DayTypeAssignmentsRelStructure | None = field(
        default=None,
        metadata={
            "name": "dayTypeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
