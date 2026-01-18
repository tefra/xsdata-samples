from __future__ import annotations

from dataclasses import dataclass, field

from .blocks_in_frame_rel_structure import BlocksInFrameRelStructure
from .common_version_frame_structure import CommonVersionFrameStructure
from .courses_of_journeys_in_frame_rel_structure import (
    CoursesOfJourneysInFrameRelStructure,
)
from .relief_opportunities_in_frame_rel_structure import (
    ReliefOpportunitiesInFrameRelStructure,
)
from .service_calendar_frame_ref import ServiceCalendarFrameRef
from .vehicle_services_in_frame_rel_structure import (
    VehicleServicesInFrameRelStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleScheduleVersionFrameStructure(CommonVersionFrameStructure):
    class Meta:
        name = "VehicleSchedule_VersionFrameStructure"

    service_calendar_frame_ref: None | ServiceCalendarFrameRef = field(
        default=None,
        metadata={
            "name": "ServiceCalendarFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    blocks: None | BlocksInFrameRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    courses_of_journeys: None | CoursesOfJourneysInFrameRelStructure = field(
        default=None,
        metadata={
            "name": "coursesOfJourneys",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    vehicle_services: None | VehicleServicesInFrameRelStructure = field(
        default=None,
        metadata={
            "name": "vehicleServices",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    relief_opportunities: None | ReliefOpportunitiesInFrameRelStructure = (
        field(
            default=None,
            metadata={
                "name": "reliefOpportunities",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
