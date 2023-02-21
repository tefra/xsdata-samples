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
    type_of_fare_product_ref_or_types_of_fare_product: List[object] = field(
        default_factory=list,
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
            "max_occurs": 2,
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
    condition_summary: Optional[ConditionSummary] = field(
        default=None,
        metadata={
            "name": "ConditionSummary",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    supplement_product_ref: Optional[SupplementProductRef] = field(
        default=None,
        metadata={
            "name": "SupplementProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    preassigned_fare_product_ref: Optional[PreassignedFareProductRef] = field(
        default=None,
        metadata={
            "name": "PreassignedFareProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    amount_of_price_unit_product_ref: Optional[AmountOfPriceUnitProductRef] = field(
        default=None,
        metadata={
            "name": "AmountOfPriceUnitProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    usage_discount_right_ref: Optional[UsageDiscountRightRef] = field(
        default=None,
        metadata={
            "name": "UsageDiscountRightRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    third_party_product_ref: Optional[ThirdPartyProductRef] = field(
        default=None,
        metadata={
            "name": "ThirdPartyProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    capped_discount_right_ref: Optional[CappedDiscountRightRef] = field(
        default=None,
        metadata={
            "name": "CappedDiscountRightRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sale_discount_right_ref: Optional[SaleDiscountRightRef] = field(
        default=None,
        metadata={
            "name": "SaleDiscountRightRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_product_ref: Optional[FareProductRef] = field(
        default=None,
        metadata={
            "name": "FareProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context: List[object] = field(
        default_factory=list,
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
            "max_occurs": 3,
        }
    )
    validable_elements: Optional[ValidableElementsRelStructure] = field(
        default=None,
        metadata={
            "name": "validableElements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    access_rights_in_product: Optional[AccessRightsInProductRelStructure] = field(
        default=None,
        metadata={
            "name": "accessRightsInProduct",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    tariffs: Optional[TariffRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    prices: Optional[FareProductPricesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
