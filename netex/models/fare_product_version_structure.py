from dataclasses import dataclass, field
from typing import Optional
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
    transport_organisation_ref: Optional[TransportOrganisationRef] = field(
        default=None,
        metadata={
            "name": "TransportOrganisationRef",
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
    validity_parameter_assignments: Optional[GenericParameterAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "validityParameterAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    generic_parameter_assignment: Optional[GenericParameterAssignment] = field(
        default=None,
        metadata={
            "name": "GenericParameterAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    generic_parameter_assignment_in_context: Optional[GenericParameterAssignmentInContext] = field(
        default=None,
        metadata={
            "name": "GenericParameterAssignmentInContext",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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
