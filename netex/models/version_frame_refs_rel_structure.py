from dataclasses import dataclass, field
from typing import List
from netex.models.composite_frame_ref import CompositeFrameRef
from netex.models.driver_schedule_frame_ref import DriverScheduleFrameRef
from netex.models.fare_frame_ref import FareFrameRef
from netex.models.general_frame_ref import GeneralFrameRef
from netex.models.infrastructure_frame_ref import InfrastructureFrameRef
from netex.models.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.models.resource_frame_ref import ResourceFrameRef
from netex.models.sales_transaction_frame_ref import SalesTransactionFrameRef
from netex.models.service_calendar_frame_ref import ServiceCalendarFrameRef
from netex.models.service_frame_ref import ServiceFrameRef
from netex.models.site_frame_ref import SiteFrameRef
from netex.models.timetable_frame_ref import TimetableFrameRef
from netex.models.vehicle_schedule_frame_ref import VehicleScheduleFrameRef
from netex.models.version_frame_ref import VersionFrameRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VersionFrameRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "versionFrameRefs_RelStructure"

    sales_transaction_frame_ref: List[SalesTransactionFrameRef] = field(
        default_factory=list,
        metadata={
            "name": "SalesTransactionFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    fare_frame_ref: List[FareFrameRef] = field(
        default_factory=list,
        metadata={
            "name": "FareFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    service_frame_ref: List[ServiceFrameRef] = field(
        default_factory=list,
        metadata={
            "name": "ServiceFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    driver_schedule_frame_ref: List[DriverScheduleFrameRef] = field(
        default_factory=list,
        metadata={
            "name": "DriverScheduleFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    vehicle_schedule_frame_ref: List[VehicleScheduleFrameRef] = field(
        default_factory=list,
        metadata={
            "name": "VehicleScheduleFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    timetable_frame_ref: List[TimetableFrameRef] = field(
        default_factory=list,
        metadata={
            "name": "TimetableFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    site_frame_ref: List[SiteFrameRef] = field(
        default_factory=list,
        metadata={
            "name": "SiteFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    infrastructure_frame_ref: List[InfrastructureFrameRef] = field(
        default_factory=list,
        metadata={
            "name": "InfrastructureFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    general_frame_ref: List[GeneralFrameRef] = field(
        default_factory=list,
        metadata={
            "name": "GeneralFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    resource_frame_ref: List[ResourceFrameRef] = field(
        default_factory=list,
        metadata={
            "name": "ResourceFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    service_calendar_frame_ref: List[ServiceCalendarFrameRef] = field(
        default_factory=list,
        metadata={
            "name": "ServiceCalendarFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    composite_frame_ref: List[CompositeFrameRef] = field(
        default_factory=list,
        metadata={
            "name": "CompositeFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    version_frame_ref: List[VersionFrameRef] = field(
        default_factory=list,
        metadata={
            "name": "VersionFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
