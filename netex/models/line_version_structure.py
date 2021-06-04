from dataclasses import dataclass, field
from typing import List, Optional
from netex.models.accessibility_assessment import AccessibilityAssessment
from netex.models.all_vehicle_modes_of_transport_enumeration import AllVehicleModesOfTransportEnumeration
from netex.models.allowed_line_directions_rel_structure import AllowedLineDirectionsRelStructure
from netex.models.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.models.authority_ref import AuthorityRef
from netex.models.contact_structure import ContactStructure
from netex.models.external_object_ref_structure import ExternalObjectRefStructure
from netex.models.group_of_lines_ref_structure import GroupOfLinesRefStructure
from netex.models.info_links_rel_structure import InfoLinksRelStructure
from netex.models.line_type_enumeration import LineTypeEnumeration
from netex.models.mode_refs_rel_structure import ModeRefsRelStructure
from netex.models.multilingual_string import MultilingualString
from netex.models.notice_assignments_rel_structure import NoticeAssignmentsRelStructure
from netex.models.operational_context_ref import OperationalContextRef
from netex.models.operator_ref import OperatorRef
from netex.models.payment_method_enumeration import PaymentMethodEnumeration
from netex.models.presentation_structure import PresentationStructure
from netex.models.print_presentation_structure import PrintPresentationStructure
from netex.models.private_code import PrivateCode
from netex.models.purchase_moment_enumeration import PurchaseMomentEnumeration
from netex.models.route_refs_rel_structure import RouteRefsRelStructure
from netex.models.transport_organisation_refs_rel_structure import TransportOrganisationRefsRelStructure
from netex.models.transport_submode import TransportSubmode
from netex.models.type_of_line_ref import TypeOfLineRef
from netex.models.type_of_payment_method_value_structure import TypeOfPaymentMethodValueStructure
from netex.models.type_of_product_category_ref import TypeOfProductCategoryRef
from netex.models.type_of_service_ref import TypeOfServiceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LineVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "Line_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    short_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
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
    url: Optional[str] = field(
        default=None,
        metadata={
            "name": "Url",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    public_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PublicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    external_line_ref: Optional[ExternalObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "ExternalLineRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    authority_ref: Optional[AuthorityRef] = field(
        default=None,
        metadata={
            "name": "AuthorityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    operator_ref: Optional[OperatorRef] = field(
        default=None,
        metadata={
            "name": "OperatorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    additional_operators: Optional[TransportOrganisationRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "additionalOperators",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    other_modes: Optional[ModeRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "otherModes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    operational_context_ref: Optional[OperationalContextRef] = field(
        default=None,
        metadata={
            "name": "OperationalContextRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    line_type: Optional[LineTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "LineType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_line_ref: Optional[TypeOfLineRef] = field(
        default=None,
        metadata={
            "name": "TypeOfLineRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    external_product_category_ref: Optional[ExternalObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "ExternalProductCategoryRef",
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
    monitored: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Monitored",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    routes: Optional[RouteRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    represented_by_group_ref: Optional[GroupOfLinesRefStructure] = field(
        default=None,
        metadata={
            "name": "RepresentedByGroupRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    presentation: Optional[PresentationStructure] = field(
        default=None,
        metadata={
            "name": "Presentation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    alternative_presentation: Optional[PresentationStructure] = field(
        default=None,
        metadata={
            "name": "AlternativePresentation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    printed_presentation: Optional[PrintPresentationStructure] = field(
        default=None,
        metadata={
            "name": "PrintedPresentation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    payment_methods: List[PaymentMethodEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "PaymentMethods",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    types_of_payment_method: Optional[TypeOfPaymentMethodValueStructure] = field(
        default=None,
        metadata={
            "name": "typesOfPaymentMethod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    purchase_moment: List[PurchaseMomentEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "PurchaseMoment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    contact_details: Optional[ContactStructure] = field(
        default=None,
        metadata={
            "name": "ContactDetails",
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
    allowed_directions: Optional[AllowedLineDirectionsRelStructure] = field(
        default=None,
        metadata={
            "name": "allowedDirections",
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
    document_links: Optional[InfoLinksRelStructure] = field(
        default=None,
        metadata={
            "name": "documentLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
