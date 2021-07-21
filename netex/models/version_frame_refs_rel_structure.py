from dataclasses import dataclass, field
from typing import List
from .composite_frame_ref import CompositeFrameRef
from .driver_schedule_frame_ref import DriverScheduleFrameRef
from .fare_frame_ref import FareFrameRef
from .general_frame_ref import GeneralFrameRef
from .infrastructure_frame_ref import InfrastructureFrameRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .resource_frame_ref import ResourceFrameRef
from .sales_transaction_frame_ref import SalesTransactionFrameRef
from .service_calendar_frame_ref import ServiceCalendarFrameRef
from .service_frame_ref import ServiceFrameRef
from .site_frame_ref import SiteFrameRef
from .timetable_frame_ref import TimetableFrameRef
from .vehicle_schedule_frame_ref import VehicleScheduleFrameRef
from .version_frame_ref import VersionFrameRef

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
        }
    )
    fare_frame_ref: List[FareFrameRef] = field(
        default_factory=list,
        metadata={
            "name": "FareFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_frame_ref: List[ServiceFrameRef] = field(
        default_factory=list,
        metadata={
            "name": "ServiceFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    driver_schedule_frame_ref: List[DriverScheduleFrameRef] = field(
        default_factory=list,
        metadata={
            "name": "DriverScheduleFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_schedule_frame_ref: List[VehicleScheduleFrameRef] = field(
        default_factory=list,
        metadata={
            "name": "VehicleScheduleFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    timetable_frame_ref: List[TimetableFrameRef] = field(
        default_factory=list,
        metadata={
            "name": "TimetableFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    site_frame_ref: List[SiteFrameRef] = field(
        default_factory=list,
        metadata={
            "name": "SiteFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    infrastructure_frame_ref: List[InfrastructureFrameRef] = field(
        default_factory=list,
        metadata={
            "name": "InfrastructureFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    general_frame_ref: List[GeneralFrameRef] = field(
        default_factory=list,
        metadata={
            "name": "GeneralFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    resource_frame_ref: List[ResourceFrameRef] = field(
        default_factory=list,
        metadata={
            "name": "ResourceFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_calendar_frame_ref: List[ServiceCalendarFrameRef] = field(
        default_factory=list,
        metadata={
            "name": "ServiceCalendarFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    composite_frame_ref: List[CompositeFrameRef] = field(
        default_factory=list,
        metadata={
            "name": "CompositeFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    version_frame_ref: List[VersionFrameRef] = field(
        default_factory=list,
        metadata={
            "name": "VersionFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
