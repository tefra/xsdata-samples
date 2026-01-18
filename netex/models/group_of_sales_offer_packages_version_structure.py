from __future__ import annotations

from dataclasses import dataclass, field

from .alternative_names_rel_structure import AlternativeNamesRelStructure
from .condition_summary import ConditionSummary
from .discounting_rule_ref import DiscountingRuleRef
from .distribution_assignments_rel_structure import (
    DistributionAssignmentsRelStructure,
)
from .generic_parameter_assignments_rel_structure import (
    GenericParameterAssignmentsRelStructure,
)
from .group_of_entities_version_structure import (
    GroupOfEntitiesVersionStructure,
)
from .limiting_rule_ref import LimitingRuleRef
from .notice_assignments_rel_structure import NoticeAssignmentsRelStructure
from .priceable_object_version_structure import (
    FareTablesRelStructure,
    PriceGroupsRelStructure,
)
from .pricing_rule_ref import PricingRuleRef
from .pricing_service_ref import PricingServiceRef
from .rounding_ref import RoundingRef
from .sales_offer_package_elements_rel_structure import (
    SalesOfferPackageElementsRelStructure,
)
from .sales_offer_package_prices_rel_structure import (
    SalesOfferPackagePricesRelStructure,
)
from .sales_offer_package_refs_rel_structure import (
    SalesOfferPackageRefsRelStructure,
)
from .type_of_sales_offer_package_ref import TypeOfSalesOfferPackageRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupOfSalesOfferPackagesVersionStructure(
    GroupOfEntitiesVersionStructure
):
    class Meta:
        name = "GroupOfSalesOfferPackages_VersionStructure"

    alternative_names: AlternativeNamesRelStructure | None = field(
        default=None,
        metadata={
            "name": "alternativeNames",
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
    pricing_service_ref: PricingServiceRef | None = field(
        default=None,
        metadata={
            "name": "PricingServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    discounting_rule_ref_or_pricing_rule_ref: (
        LimitingRuleRef | DiscountingRuleRef | PricingRuleRef | None
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "LimitingRuleRef",
                    "type": LimitingRuleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DiscountingRuleRef",
                    "type": DiscountingRuleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PricingRuleRef",
                    "type": PricingRuleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    price_groups: PriceGroupsRelStructure | None = field(
        default=None,
        metadata={
            "name": "priceGroups",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_tables: FareTablesRelStructure | None = field(
        default=None,
        metadata={
            "name": "fareTables",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_sales_offer_package_ref: TypeOfSalesOfferPackageRef | None = field(
        default=None,
        metadata={
            "name": "TypeOfSalesOfferPackageRef",
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
    distribution_assignments: DistributionAssignmentsRelStructure | None = (
        field(
            default=None,
            metadata={
                "name": "distributionAssignments",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    rounding_ref: RoundingRef | None = field(
        default=None,
        metadata={
            "name": "RoundingRef",
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
    sales_offer_package_elements: (
        SalesOfferPackageElementsRelStructure | None
    ) = field(
        default=None,
        metadata={
            "name": "salesOfferPackageElements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    members: SalesOfferPackageRefsRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
