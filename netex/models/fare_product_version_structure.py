from dataclasses import dataclass, field

from .access_rights_in_product_rel_structure import (
    AccessRightsInProductRelStructure,
)
from .amount_of_price_unit_product_ref import AmountOfPriceUnitProductRef
from .authority_ref import AuthorityRef
from .capped_discount_right_ref import CappedDiscountRightRef
from .charging_moment_enumeration import ChargingMomentEnumeration
from .charging_moment_ref import ChargingMomentRef
from .condition_summary import ConditionSummary
from .fare_product_prices_rel_structure import FareProductPricesRelStructure
from .fare_product_ref import FareProductRef
from .general_organisation_ref import GeneralOrganisationRef
from .generic_parameter_assignments_rel_structure import (
    GenericParameterAssignment,
    GenericParameterAssignmentInContext,
    GenericParameterAssignmentsRelStructure,
)
from .management_agent_ref import ManagementAgentRef
from .online_service_operator_ref import OnlineServiceOperatorRef
from .operator_ref import OperatorRef
from .organisation_ref import OrganisationRef
from .other_organisation_ref import OtherOrganisationRef
from .preassigned_fare_product_ref import PreassignedFareProductRef
from .retail_consortium_ref import RetailConsortiumRef
from .sale_discount_right_ref import SaleDiscountRightRef
from .service_access_right_version_structure import (
    ServiceAccessRightVersionStructure,
)
from .serviced_organisation_ref import ServicedOrganisationRef
from .supplement_product_ref import SupplementProductRef
from .tariff_refs_rel_structure import TariffRefsRelStructure
from .third_party_product_ref import ThirdPartyProductRef
from .travel_agent_ref import TravelAgentRef
from .type_of_fare_product_ref import TypeOfFareProductRef
from .type_of_fare_product_refs_rel_structure import (
    TypeOfFareProductRefsRelStructure,
)
from .usage_discount_right_ref import UsageDiscountRightRef
from .validable_elements_rel_structure import ValidableElementsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareProductVersionStructure(ServiceAccessRightVersionStructure):
    class Meta:
        name = "FareProduct_VersionStructure"

    charging_moment_ref: ChargingMomentRef | None = field(
        default=None,
        metadata={
            "name": "ChargingMomentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    charging_moment_type: ChargingMomentEnumeration | None = field(
        default=None,
        metadata={
            "name": "ChargingMomentType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_fare_product_ref_or_types_of_fare_product: (
        TypeOfFareProductRef | TypeOfFareProductRefsRelStructure | None
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TypeOfFareProductRef",
                    "type": TypeOfFareProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "typesOfFareProduct",
                    "type": TypeOfFareProductRefsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    organisation_ref_or_other_organisation_ref_or_transport_organisation_ref: (
        RetailConsortiumRef
        | OnlineServiceOperatorRef
        | GeneralOrganisationRef
        | ManagementAgentRef
        | ServicedOrganisationRef
        | TravelAgentRef
        | OtherOrganisationRef
        | AuthorityRef
        | OperatorRef
        | OrganisationRef
        | None
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "RetailConsortiumRef",
                    "type": RetailConsortiumRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OnlineServiceOperatorRef",
                    "type": OnlineServiceOperatorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeneralOrganisationRef",
                    "type": GeneralOrganisationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ManagementAgentRef",
                    "type": ManagementAgentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServicedOrganisationRef",
                    "type": ServicedOrganisationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TravelAgentRef",
                    "type": TravelAgentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OtherOrganisationRef",
                    "type": OtherOrganisationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AuthorityRef",
                    "type": AuthorityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatorRef",
                    "type": OperatorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OrganisationRef",
                    "type": OrganisationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    condition_summary: ConditionSummary | None = field(
        default=None,
        metadata={
            "name": "ConditionSummary",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    preassigned_fare_product_ref_or_fare_product_ref_or_sale_discount_right_ref: (
        SupplementProductRef
        | PreassignedFareProductRef
        | AmountOfPriceUnitProductRef
        | UsageDiscountRightRef
        | ThirdPartyProductRef
        | CappedDiscountRightRef
        | SaleDiscountRightRef
        | FareProductRef
        | None
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SupplementProductRef",
                    "type": SupplementProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PreassignedFareProductRef",
                    "type": PreassignedFareProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AmountOfPriceUnitProductRef",
                    "type": AmountOfPriceUnitProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UsageDiscountRightRef",
                    "type": UsageDiscountRightRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ThirdPartyProductRef",
                    "type": ThirdPartyProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CappedDiscountRightRef",
                    "type": CappedDiscountRightRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SaleDiscountRightRef",
                    "type": SaleDiscountRightRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareProductRef",
                    "type": FareProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context: (
        GenericParameterAssignmentsRelStructure
        | GenericParameterAssignment
        | GenericParameterAssignmentInContext
        | None
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "validityParameterAssignments",
                    "type": GenericParameterAssignmentsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GenericParameterAssignment",
                    "type": GenericParameterAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GenericParameterAssignmentInContext",
                    "type": GenericParameterAssignmentInContext,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    validable_elements: ValidableElementsRelStructure | None = field(
        default=None,
        metadata={
            "name": "validableElements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    access_rights_in_product: AccessRightsInProductRelStructure | None = field(
        default=None,
        metadata={
            "name": "accessRightsInProduct",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    tariffs: TariffRefsRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    prices: FareProductPricesRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
