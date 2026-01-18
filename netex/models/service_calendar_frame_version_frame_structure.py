from dataclasses import dataclass, field
from typing import Optional

from .common_version_frame_structure import CommonVersionFrameStructure
from .day_type_assignments_in_frame_rel_structure import (
    DayTypeAssignmentsInFrameRelStructure,
)
from .day_types_in_frame_rel_structure import DayTypesInFrameRelStructure
from .group_of_timebands_in_frame_rel_structure import (
    GroupOfTimebandsInFrameRelStructure,
)
from .operating_days_in_frame_rel_structure import (
    OperatingDaysInFrameRelStructure,
)
from .operating_periods_in_frame_rel_structure import (
    OperatingPeriodsInFrameRelStructure,
)
from .service_calendar import ServiceCalendar
from .timebands_in_frame_rel_structure import TimebandsInFrameRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ServiceCalendarFrameVersionFrameStructure(CommonVersionFrameStructure):
    class Meta:
        name = "ServiceCalendarFrame_VersionFrameStructure"

    service_calendar: ServiceCalendar | None = field(
        default=None,
        metadata={
            "name": "ServiceCalendar",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    day_types: DayTypesInFrameRelStructure | None = field(
        default=None,
        metadata={
            "name": "dayTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    timebands: TimebandsInFrameRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    group_of_timebands: GroupOfTimebandsInFrameRelStructure | None = field(
        default=None,
        metadata={
            "name": "groupOfTimebands",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    operating_days: OperatingDaysInFrameRelStructure | None = field(
        default=None,
        metadata={
            "name": "operatingDays",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    operating_periods: OperatingPeriodsInFrameRelStructure | None = field(
        default=None,
        metadata={
            "name": "operatingPeriods",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    day_type_assignments: DayTypeAssignmentsInFrameRelStructure | None = (
        field(
            default=None,
            metadata={
                "name": "dayTypeAssignments",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
