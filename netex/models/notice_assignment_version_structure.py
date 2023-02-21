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

    notice_ref_or_group_of_notices_ref_or_notice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "NoticeRef",
                    "type": NoticeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfNoticesRef",
                    "type": GeneralGroupOfEntitiesRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Notice",
                    "type": Notice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 3,
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
    navigation_path_ref: Optional[NavigationPathRef] = field(
        default=None,
        metadata={
            "name": "NavigationPathRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_journey_pattern_ref: Optional[ServiceJourneyPatternRef] = field(
        default=None,
        metadata={
            "name": "ServiceJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_pattern_ref: Optional[ServicePatternRef] = field(
        default=None,
        metadata={
            "name": "ServicePatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    dead_run_journey_pattern_ref: Optional[DeadRunJourneyPatternRef] = field(
        default=None,
        metadata={
            "name": "DeadRunJourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journey_pattern_ref: Optional[JourneyPatternRef] = field(
        default=None,
        metadata={
            "name": "JourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    timing_pattern_ref: Optional[TimingPatternRef] = field(
        default=None,
        metadata={
            "name": "TimingPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    route_ref: Optional[RouteRef] = field(
        default=None,
        metadata={
            "name": "RouteRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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
    parent_common_section_ref: Optional[ParentCommonSectionRef] = field(
        default=None,
        metadata={
            "name": "ParentCommonSectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    common_section_ref: Optional[CommonSectionRef] = field(
        default=None,
        metadata={
            "name": "CommonSectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    line_section_ref: Optional[LineSectionRef] = field(
        default=None,
        metadata={
            "name": "LineSectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_section_ref: Optional[FareSectionRef] = field(
        default=None,
        metadata={
            "name": "FareSectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    general_section_ref: Optional[GeneralSectionRef] = field(
        default=None,
        metadata={
            "name": "GeneralSectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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
