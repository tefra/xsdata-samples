from dataclasses import dataclass, field
from typing import List, Optional
from .assignment_version_structure_1 import AssignmentVersionStructure1
from .common_section_ref import CommonSectionRef
from .dated_special_service_ref import DatedSpecialServiceRef
from .dated_vehicle_journey_ref import DatedVehicleJourneyRef
from .dead_run_journey_pattern_ref import DeadRunJourneyPatternRef
from .dead_run_ref import DeadRunRef
from .fare_section_ref import FareSectionRef
from .general_group_of_entities_ref_structure import GeneralGroupOfEntitiesRefStructure
from .general_section_ref import GeneralSectionRef
from .journey_pattern_ref import JourneyPatternRef
from .journey_ref import JourneyRef
from .line_section_ref import LineSectionRef
from .link_sequence_ref import LinkSequenceRef
from .navigation_path_ref import NavigationPathRef
from .notice import Notice
from .notice_ref import NoticeRef
from .parent_common_section_ref import ParentCommonSectionRef
from .point_in_sequence_ref_structure import PointInSequenceRefStructure
from .publicity_channel_enumeration import PublicityChannelEnumeration
from .route_ref import RouteRef
from .section_ref import SectionRef
from .service_journey_pattern_ref import ServiceJourneyPatternRef
from .service_journey_ref import ServiceJourneyRef
from .service_pattern_ref import ServicePatternRef
from .special_service_ref import SpecialServiceRef
from .template_service_journey_ref import TemplateServiceJourneyRef
from .timing_pattern_ref import TimingPatternRef
from .vehicle_journey_ref import VehicleJourneyRef
from .version_of_object_ref_structure import VersionOfObjectRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class NoticeAssignmentVersionStructure(AssignmentVersionStructure1):
    class Meta:
        name = "NoticeAssignment_VersionStructure"

    notice_ref: Optional[NoticeRef] = field(
        default=None,
        metadata={
            "name": "NoticeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_of_notices_ref: Optional[GeneralGroupOfEntitiesRefStructure] = field(
        default=None,
        metadata={
            "name": "GroupOfNoticesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    notice: Optional[Notice] = field(
        default=None,
        metadata={
            "name": "Notice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    noticed_object_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "NoticedObjectRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    dated_vehicle_journey_ref: List[DatedVehicleJourneyRef] = field(
        default_factory=list,
        metadata={
            "name": "DatedVehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 6,
            "sequential": True,
        }
    )
    dated_special_service_ref: List[DatedSpecialServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "DatedSpecialServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 10,
            "sequential": True,
        }
    )
    special_service_ref: List[SpecialServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "SpecialServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 6,
            "sequential": True,
        }
    )
    template_service_journey_ref: List[TemplateServiceJourneyRef] = field(
        default_factory=list,
        metadata={
            "name": "TemplateServiceJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 10,
            "sequential": True,
        }
    )
    service_journey_ref: List[ServiceJourneyRef] = field(
        default_factory=list,
        metadata={
            "name": "ServiceJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 6,
            "sequential": True,
        }
    )
    dead_run_ref: List[DeadRunRef] = field(
        default_factory=list,
        metadata={
            "name": "DeadRunRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 10,
            "sequential": True,
        }
    )
    vehicle_journey_ref: List[VehicleJourneyRef] = field(
        default_factory=list,
        metadata={
            "name": "VehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 6,
            "sequential": True,
        }
    )
    journey_ref: List[JourneyRef] = field(
        default_factory=list,
        metadata={
            "name": "JourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    navigation_path_ref: List[NavigationPathRef] = field(
        default_factory=list,
        metadata={
            "name": "NavigationPathRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    service_journey_pattern_ref: List[ServiceJourneyPatternRef] = field(
        default_factory=list,
        metadata={
            "name": "ServiceJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 6,
            "sequential": True,
        }
    )
    service_pattern_ref: List[ServicePatternRef] = field(
        default_factory=list,
        metadata={
            "name": "ServicePatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 6,
            "sequential": True,
        }
    )
    dead_run_journey_pattern_ref: List[DeadRunJourneyPatternRef] = field(
        default_factory=list,
        metadata={
            "name": "DeadRunJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 6,
            "sequential": True,
        }
    )
    journey_pattern_ref: List[JourneyPatternRef] = field(
        default_factory=list,
        metadata={
            "name": "JourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    timing_pattern_ref: List[TimingPatternRef] = field(
        default_factory=list,
        metadata={
            "name": "TimingPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    route_ref: List[RouteRef] = field(
        default_factory=list,
        metadata={
            "name": "RouteRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    link_sequence_ref: Optional[LinkSequenceRef] = field(
        default=None,
        metadata={
            "name": "LinkSequenceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parent_common_section_ref: List[ParentCommonSectionRef] = field(
        default_factory=list,
        metadata={
            "name": "ParentCommonSectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    common_section_ref: List[CommonSectionRef] = field(
        default_factory=list,
        metadata={
            "name": "CommonSectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    line_section_ref: List[LineSectionRef] = field(
        default_factory=list,
        metadata={
            "name": "LineSectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    fare_section_ref: List[FareSectionRef] = field(
        default_factory=list,
        metadata={
            "name": "FareSectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 6,
            "sequential": True,
        }
    )
    general_section_ref: List[GeneralSectionRef] = field(
        default_factory=list,
        metadata={
            "name": "GeneralSectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    section_ref: Optional[SectionRef] = field(
        default=None,
        metadata={
            "name": "SectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    start_point_in_pattern_ref: Optional[PointInSequenceRefStructure] = field(
        default=None,
        metadata={
            "name": "StartPointInPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    end_point_in_pattern_ref: Optional[PointInSequenceRefStructure] = field(
        default=None,
        metadata={
            "name": "EndPointInPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    mark: Optional[str] = field(
        default=None,
        metadata={
            "name": "Mark",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    mark_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "MarkUrl",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    publicity_channel: Optional[PublicityChannelEnumeration] = field(
        default=None,
        metadata={
            "name": "PublicityChannel",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    advertised: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Advertised",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
