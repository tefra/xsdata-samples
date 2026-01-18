from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .accessibility_assessment import AccessibilityAssessment
from .all_vehicle_modes_of_transport_enumeration import (
    AllVehicleModesOfTransportEnumeration,
)
from .allowed_line_directions_rel_structure import (
    AllowedLineDirectionsRelStructure,
)
from .authority_ref import AuthorityRef
from .contact_structure import ContactStructure
from .entity_in_version_structure import DataManagedObjectStructure
from .external_object_ref_structure import ExternalObjectRefStructure
from .group_of_lines_ref_structure import GroupOfLinesRefStructure
from .info_links_rel_structure import InfoLinksRelStructure
from .line_type_enumeration import LineTypeEnumeration
from .mode_refs_rel_structure import ModeRefsRelStructure
from .multilingual_string import MultilingualString
from .notice_assignments_rel_structure import NoticeAssignmentsRelStructure
from .operational_context_ref import OperationalContextRef
from .operator_ref import OperatorRef
from .payment_method_enumeration import PaymentMethodEnumeration
from .presentation_structure import PresentationStructure
from .print_presentation_structure import PrintPresentationStructure
from .private_code import PrivateCode
from .purchase_moment_enumeration import PurchaseMomentEnumeration
from .route_refs_rel_structure import RouteRefsRelStructure
from .transport_organisation_refs_rel_structure import (
    TransportOrganisationRefsRelStructure,
)
from .transport_submode import TransportSubmode
from .type_of_line_ref import TypeOfLineRef
from .type_of_payment_method_value_structure import (
    TypeOfPaymentMethodValueStructure,
)
from .type_of_product_category_ref import TypeOfProductCategoryRef
from .type_of_service_ref import TypeOfServiceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LineVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "Line_VersionStructure"

    name: MultilingualString = field(
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    short_name: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    transport_mode: None | AllVehicleModesOfTransportEnumeration = field(
        default=None,
        metadata={
            "name": "TransportMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    transport_submode: None | TransportSubmode = field(
        default=None,
        metadata={
            "name": "TransportSubmode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    url: None | str = field(
        default=None,
        metadata={
            "name": "Url",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    public_code: None | str = field(
        default=None,
        metadata={
            "name": "PublicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    private_code: None | PrivateCode = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    external_line_ref: None | ExternalObjectRefStructure = field(
        default=None,
        metadata={
            "name": "ExternalLineRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    authority_ref: None | AuthorityRef = field(
        default=None,
        metadata={
            "name": "AuthorityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    operator_ref: None | OperatorRef = field(
        default=None,
        metadata={
            "name": "OperatorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    additional_operators: None | TransportOrganisationRefsRelStructure = field(
        default=None,
        metadata={
            "name": "additionalOperators",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    other_modes: None | ModeRefsRelStructure = field(
        default=None,
        metadata={
            "name": "otherModes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    operational_context_ref: None | OperationalContextRef = field(
        default=None,
        metadata={
            "name": "OperationalContextRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    line_type: None | LineTypeEnumeration = field(
        default=None,
        metadata={
            "name": "LineType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_line_ref: None | TypeOfLineRef = field(
        default=None,
        metadata={
            "name": "TypeOfLineRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    external_product_category_ref: None | ExternalObjectRefStructure = field(
        default=None,
        metadata={
            "name": "ExternalProductCategoryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_product_category_ref: None | TypeOfProductCategoryRef = field(
        default=None,
        metadata={
            "name": "TypeOfProductCategoryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_service_ref: None | TypeOfServiceRef = field(
        default=None,
        metadata={
            "name": "TypeOfServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    monitored: None | bool = field(
        default=None,
        metadata={
            "name": "Monitored",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    routes: None | RouteRefsRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    represented_by_group_ref: None | GroupOfLinesRefStructure = field(
        default=None,
        metadata={
            "name": "RepresentedByGroupRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    presentation: None | PresentationStructure = field(
        default=None,
        metadata={
            "name": "Presentation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    alternative_presentation: None | PresentationStructure = field(
        default=None,
        metadata={
            "name": "AlternativePresentation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    printed_presentation: None | PrintPresentationStructure = field(
        default=None,
        metadata={
            "name": "PrintedPresentation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    payment_methods: Iterable[PaymentMethodEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "PaymentMethods",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    types_of_payment_method: None | TypeOfPaymentMethodValueStructure = field(
        default=None,
        metadata={
            "name": "typesOfPaymentMethod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    purchase_moment: Iterable[PurchaseMomentEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "PurchaseMoment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    contact_details: None | ContactStructure = field(
        default=None,
        metadata={
            "name": "ContactDetails",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    accessibility_assessment: None | AccessibilityAssessment = field(
        default=None,
        metadata={
            "name": "AccessibilityAssessment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    allowed_directions: None | AllowedLineDirectionsRelStructure = field(
        default=None,
        metadata={
            "name": "allowedDirections",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    notice_assignments: None | NoticeAssignmentsRelStructure = field(
        default=None,
        metadata={
            "name": "noticeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    document_links: None | InfoLinksRelStructure = field(
        default=None,
        metadata={
            "name": "documentLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
