from dataclasses import dataclass, field
from typing import List, Optional
from .alternative_names_rel_structure import AlternativeNamesRelStructure
from .cell_versioned_child_structure import (
    FareTablesRelStructure,
    PriceGroupsRelStructure,
)
from .condition_summary import ConditionSummary
from .discounting_rule_ref import DiscountingRuleRef
from .distribution_assignments_rel_structure import DistributionAssignmentsRelStructure
from .generic_parameter_assignment_version_structure import GenericParameterAssignmentsRelStructure
from .group_of_entities_version_structure import GroupOfEntitiesVersionStructure
from .limiting_rule_ref import LimitingRuleRef
from .notice_assignments_rel_structure import NoticeAssignmentsRelStructure
from .pricing_rule_ref import PricingRuleRef
from .pricing_service_ref import PricingServiceRef
from .rounding_ref import RoundingRef
from .sales_offer_package_elements_rel_structure import SalesOfferPackageElementsRelStructure
from .sales_offer_package_prices_rel_structure import SalesOfferPackagePricesRelStructure
from .sales_offer_package_refs_rel_structure import SalesOfferPackageRefsRelStructure
from .type_of_sales_offer_package_ref import TypeOfSalesOfferPackageRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupOfSalesOfferPackagesVersionStructure(GroupOfEntitiesVersionStructure):
    class Meta:
        name = "GroupOfSalesOfferPackages_VersionStructure"

    alternative_names: Optional[AlternativeNamesRelStructure] = field(
        default=None,
        metadata={
            "name": "alternativeNames",
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
    pricing_service_ref: Optional[PricingServiceRef] = field(
        default=None,
        metadata={
            "name": "PricingServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    choice: List[object] = field(
        default_factory=list,
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
                {
                    "name": "priceGroups",
                    "type": PriceGroupsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "fareTables",
                    "type": FareTablesRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfSalesOfferPackageRef",
                    "type": TypeOfSalesOfferPackageRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ConditionSummary",
                    "type": ConditionSummary,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "validityParameterAssignments",
                    "type": GenericParameterAssignmentsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "distributionAssignments",
                    "type": DistributionAssignmentsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoundingRef",
                    "type": RoundingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "prices",
                    "type": SalesOfferPackagePricesRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "salesOfferPackageElements",
                    "type": SalesOfferPackageElementsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "members",
                    "type": SalesOfferPackageRefsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 20,
        }
    )
