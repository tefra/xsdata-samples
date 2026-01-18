from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Union

from .composite_frame_ref import CompositeFrameRef
from .driver_schedule_frame_ref import DriverScheduleFrameRef
from .fare_frame_ref import FareFrameRef
from .general_frame_ref import GeneralFrameRef
from .infrastructure_frame_ref import InfrastructureFrameRef
from .mobility_journey_frame_ref import MobilityJourneyFrameRef
from .mobility_service_frame_ref import MobilityServiceFrameRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .resource_frame_ref import ResourceFrameRef
from .sales_transaction_frame_ref import SalesTransactionFrameRef
from .service_calendar_frame_ref import ServiceCalendarFrameRef
from .service_frame_ref import ServiceFrameRef
from .site_frame_ref import SiteFrameRef
from .timetable_frame_ref import TimetableFrameRef
from .vehicle_schedule_frame_ref import VehicleScheduleFrameRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VersionFrameRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "versionFrameRefs_RelStructure"

    version_frame_ref: Iterable[
        MobilityJourneyFrameRef | MobilityServiceFrameRef | SalesTransactionFrameRef | FareFrameRef | ServiceFrameRef | DriverScheduleFrameRef | VehicleScheduleFrameRef | TimetableFrameRef | SiteFrameRef | InfrastructureFrameRef | GeneralFrameRef | ResourceFrameRef | ServiceCalendarFrameRef | CompositeFrameRef
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "MobilityJourneyFrameRef",
                    "type": MobilityJourneyFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MobilityServiceFrameRef",
                    "type": MobilityServiceFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesTransactionFrameRef",
                    "type": SalesTransactionFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareFrameRef",
                    "type": FareFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceFrameRef",
                    "type": ServiceFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DriverScheduleFrameRef",
                    "type": DriverScheduleFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleScheduleFrameRef",
                    "type": VehicleScheduleFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimetableFrameRef",
                    "type": TimetableFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SiteFrameRef",
                    "type": SiteFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "InfrastructureFrameRef",
                    "type": InfrastructureFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeneralFrameRef",
                    "type": GeneralFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ResourceFrameRef",
                    "type": ResourceFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceCalendarFrameRef",
                    "type": ServiceCalendarFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CompositeFrameRef",
                    "type": CompositeFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
