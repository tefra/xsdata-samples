from dataclasses import dataclass, field

from .amount_of_price_unit_product_ref import AmountOfPriceUnitProductRef
from .capped_discount_right_ref import CappedDiscountRightRef
from .condition_summary import ConditionSummary
from .fare_product_ref import FareProductRef
from .generic_parameter_assignments_rel_structure import (
    GenericParameterAssignmentsRelStructure,
)
from .preassigned_fare_product_ref import PreassignedFareProductRef
from .priceable_object_version_structure import PriceableObjectVersionStructure
from .sale_discount_right_ref import SaleDiscountRightRef
from .sales_offer_package_prices_rel_structure import (
    SalesOfferPackagePricesRelStructure,
)
from .sales_offer_package_ref import SalesOfferPackageRef
from .supplement_product_ref import SupplementProductRef
from .third_party_product_ref import ThirdPartyProductRef
from .type_of_travel_document_ref import TypeOfTravelDocumentRef
from .usage_discount_right_ref import UsageDiscountRightRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SalesOfferPackageElementVersionStructure(
    PriceableObjectVersionStructure
):
    class Meta:
        name = "SalesOfferPackageElement_VersionStructure"

    requires_validation: bool | None = field(
        default=None,
        metadata={
            "name": "RequiresValidation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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
    sales_offer_package_ref: SalesOfferPackageRef | None = field(
        default=None,
        metadata={
            "name": "SalesOfferPackageRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_travel_document_ref: TypeOfTravelDocumentRef | None = field(
        default=None,
        metadata={
            "name": "TypeOfTravelDocumentRef",
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
    validity_parameter_assignments: (
        GenericParameterAssignmentsRelStructure | None
    ) = field(
        default=None,
        metadata={
            "name": "validityParameterAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    prices: SalesOfferPackagePricesRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    order: int | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
