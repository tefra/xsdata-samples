from dataclasses import dataclass, field
from typing import List, Optional
from .accessibility_assessment import AccessibilityAssessment
from .all_vehicle_modes_of_transport_enumeration import AllVehicleModesOfTransportEnumeration
from .external_object_ref_structure import ExternalObjectRefStructure
from .journey_accountings_rel_structure import JourneyAccountingsRelStructure
from .link_sequence_projection import LinkSequenceProjection
from .link_sequence_projection_ref import LinkSequenceProjectionRef
from .link_sequence_version_structure import LinkSequenceVersionStructure
from .notice_assignments_rel_structure import NoticeAssignmentsRelStructure
from .transport_submode import TransportSubmode
from .type_of_product_category_ref import TypeOfProductCategoryRef
from .type_of_service_ref import TypeOfServiceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyVersionStructure(LinkSequenceVersionStructure):
    class Meta:
        name = "Journey_VersionStructure"

    transport_mode: Optional[AllVehicleModesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "TransportMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    transport_submode: Optional[TransportSubmode] = field(
        default=None,
        metadata={
            "name": "TransportSubmode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    external_vehicle_journey_ref: Optional[ExternalObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "ExternalVehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_product_category_ref: Optional[TypeOfProductCategoryRef] = field(
        default=None,
        metadata={
            "name": "TypeOfProductCategoryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_service_ref: Optional[TypeOfServiceRef] = field(
        default=None,
        metadata={
            "name": "TypeOfServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    link_sequence_projection_ref_or_link_sequence_projection: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "LinkSequenceProjectionRef",
                    "type": LinkSequenceProjectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LinkSequenceProjection",
                    "type": LinkSequenceProjection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 2,
        }
    )
    monitored: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Monitored",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    accessibility_assessment: Optional[AccessibilityAssessment] = field(
        default=None,
        metadata={
            "name": "AccessibilityAssessment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journey_accountings: Optional[JourneyAccountingsRelStructure] = field(
        default=None,
        metadata={
            "name": "journeyAccountings",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    notice_assignments: Optional[NoticeAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "noticeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
