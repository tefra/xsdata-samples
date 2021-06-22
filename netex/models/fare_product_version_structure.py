from dataclasses import dataclass, field
from typing import List, Optional
from .access_rights_in_product_rel_structure import AccessRightsInProductRelStructure
from .amount_of_price_unit_product_ref import AmountOfPriceUnitProductRef
from .authority_ref import AuthorityRef
from .capped_discount_right_ref import CappedDiscountRightRef
from .charging_moment_enumeration import ChargingMomentEnumeration
from .charging_moment_ref import ChargingMomentRef
from .condition_summary import ConditionSummary
from .fare_product_prices_rel_structure import FareProductPricesRelStructure
from .fare_product_ref import FareProductRef
from .generic_parameter_assignment_version_structure import (
    GenericParameterAssignment,
    GenericParameterAssignmentInContext,
    GenericParameterAssignmentsRelStructure,
)
from .operator_ref import OperatorRef
from .preassigned_fare_product_ref import PreassignedFareProductRef
from .sale_discount_right_ref import SaleDiscountRightRef
from .service_access_right_version_structure import ServiceAccessRightVersionStructure
from .supplement_product_ref import SupplementProductRef
from .tariff_refs_rel_structure import TariffRefsRelStructure
from .third_party_product_ref import ThirdPartyProductRef
from .transport_organisation_ref import TransportOrganisationRef
from .type_of_fare_product_ref import TypeOfFareProductRef
from .type_of_fare_product_refs_rel_structure import TypeOfFareProductRefsRelStructure
from .usage_discount_right_ref import UsageDiscountRightRef
from .validable_elements_rel_structure import ValidableElementsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareProductVersionStructure(ServiceAccessRightVersionStructure):
    class Meta:
        name = "FareProduct_VersionStructure"

    charging_moment_ref: Optional[ChargingMomentRef] = field(
        default=None,
        metadata={
            "name": "ChargingMomentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    charging_moment_type: Optional[ChargingMomentEnumeration] = field(
        default=None,
        metadata={
            "name": "ChargingMomentType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_fare_product_ref: Optional[TypeOfFareProductRef] = field(
        default=None,
        metadata={
            "name": "TypeOfFareProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    types_of_fare_product: Optional[TypeOfFareProductRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "typesOfFareProduct",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    choice_1: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
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
                    "name": "TransportOrganisationRef",
                    "type": TransportOrganisationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ConditionSummary",
                    "type": ConditionSummary,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
                {
                    "name": "validableElements",
                    "type": ValidableElementsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "accessRightsInProduct",
                    "type": AccessRightsInProductRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "tariffs",
                    "type": TariffRefsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "prices",
                    "type": FareProductPricesRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 43,
        }
    )
