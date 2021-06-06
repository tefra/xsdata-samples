from dataclasses import dataclass, field
from typing import Optional
from .abstract_group_member_versioned_child_structure import AbstractGroupMemberVersionedChildStructure
from .dated_special_service_ref import DatedSpecialServiceRef
from .dated_vehicle_journey_ref import DatedVehicleJourneyRef
from .dead_run_ref import DeadRunRef
from .group_of_services_ref_structure import GroupOfServicesRefStructure
from .journey_designator import JourneyDesignator
from .journey_ref import JourneyRef
from .notice_assignment_views_rel_structure import NoticeAssignmentViewsRelStructure
from .service_designator import ServiceDesignator
from .service_journey_ref import ServiceJourneyRef
from .special_service_ref import SpecialServiceRef
from .template_service_journey_ref import TemplateServiceJourneyRef
from .train_number_ref import TrainNumberRef
from .vehicle_journey_ref import VehicleJourneyRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupOfServicesMemberStructure(AbstractGroupMemberVersionedChildStructure):
    group_of_services_ref: Optional[GroupOfServicesRefStructure] = field(
        default=None,
        metadata={
            "name": "GroupOfServicesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    dated_vehicle_journey_ref: Optional[DatedVehicleJourneyRef] = field(
        default=None,
        metadata={
            "name": "DatedVehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    dated_special_service_ref: Optional[DatedSpecialServiceRef] = field(
        default=None,
        metadata={
            "name": "DatedSpecialServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    special_service_ref: Optional[SpecialServiceRef] = field(
        default=None,
        metadata={
            "name": "SpecialServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    template_service_journey_ref: Optional[TemplateServiceJourneyRef] = field(
        default=None,
        metadata={
            "name": "TemplateServiceJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_journey_ref: Optional[ServiceJourneyRef] = field(
        default=None,
        metadata={
            "name": "ServiceJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    dead_run_ref: Optional[DeadRunRef] = field(
        default=None,
        metadata={
            "name": "DeadRunRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_journey_ref: Optional[VehicleJourneyRef] = field(
        default=None,
        metadata={
            "name": "VehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journey_ref: Optional[JourneyRef] = field(
        default=None,
        metadata={
            "name": "JourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    train_number_ref: Optional[TrainNumberRef] = field(
        default=None,
        metadata={
            "name": "TrainNumberRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journey_designator: Optional[JourneyDesignator] = field(
        default=None,
        metadata={
            "name": "JourneyDesignator",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_designator: Optional[ServiceDesignator] = field(
        default=None,
        metadata={
            "name": "ServiceDesignator",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    notice_assignments: Optional[NoticeAssignmentViewsRelStructure] = field(
        default=None,
        metadata={
            "name": "noticeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
