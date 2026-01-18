from dataclasses import dataclass, field

from .accessibility_assessment import AccessibilityAssessment
from .all_vehicle_modes_of_transport_enumeration import (
    AllVehicleModesOfTransportEnumeration,
)
from .external_object_ref_structure import ExternalObjectRefStructure
from .journey_accountings_rel_structure import JourneyAccountingsRelStructure
from .link_sequence_projection import LinkSequenceProjection
from .link_sequence_projection_ref import LinkSequenceProjectionRef
from .notice_assignments_rel_structure import NoticeAssignmentsRelStructure
from .sections_in_sequence_rel_structure import LinkSequenceVersionStructure
from .transport_submode import TransportSubmode
from .type_of_product_category_ref import TypeOfProductCategoryRef
from .type_of_service_ref import TypeOfServiceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class JourneyVersionStructure(LinkSequenceVersionStructure):
    class Meta:
        name = "Journey_VersionStructure"

    transport_mode: AllVehicleModesOfTransportEnumeration | None = field(
        default=None,
        metadata={
            "name": "TransportMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    transport_submode: TransportSubmode | None = field(
        default=None,
        metadata={
            "name": "TransportSubmode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    external_vehicle_journey_ref: ExternalObjectRefStructure | None = field(
        default=None,
        metadata={
            "name": "ExternalVehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_product_category_ref: TypeOfProductCategoryRef | None = field(
        default=None,
        metadata={
            "name": "TypeOfProductCategoryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_service_ref: TypeOfServiceRef | None = field(
        default=None,
        metadata={
            "name": "TypeOfServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    link_sequence_projection_ref_or_link_sequence_projection: (
        LinkSequenceProjectionRef | LinkSequenceProjection | None
    ) = field(
        default=None,
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
        },
    )
    monitored: bool | None = field(
        default=None,
        metadata={
            "name": "Monitored",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    accessibility_assessment: AccessibilityAssessment | None = field(
        default=None,
        metadata={
            "name": "AccessibilityAssessment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    journey_accountings: JourneyAccountingsRelStructure | None = field(
        default=None,
        metadata={
            "name": "journeyAccountings",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    notice_assignments: NoticeAssignmentsRelStructure | None = field(
        default=None,
        metadata={
            "name": "noticeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
