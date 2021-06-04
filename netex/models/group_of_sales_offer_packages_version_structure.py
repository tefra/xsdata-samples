from dataclasses import dataclass, field
from typing import List, Optional
from netex.models.alternative_names_rel_structure import AlternativeNamesRelStructure
from netex.models.cell_versioned_child_structure import (
    FareTablesRelStructure,
    PriceGroupsRelStructure,
)
from netex.models.condition_summary import ConditionSummary
from netex.models.discounting_rule_ref import DiscountingRuleRef
from netex.models.distribution_assignments_rel_structure import DistributionAssignmentsRelStructure
from netex.models.generic_parameter_assignment_version_structure import GenericParameterAssignmentsRelStructure
from netex.models.group_of_entities_version_structure import GroupOfEntitiesVersionStructure
from netex.models.limiting_rule_ref import LimitingRuleRef
from netex.models.notice_assignments_rel_structure import NoticeAssignmentsRelStructure
from netex.models.pricing_rule_ref import PricingRuleRef
from netex.models.pricing_service_ref import PricingServiceRef
from netex.models.rounding_ref import RoundingRef
from netex.models.sales_offer_package_elements_rel_structure import SalesOfferPackageElementsRelStructure
from netex.models.sales_offer_package_prices_rel_structure import SalesOfferPackagePricesRelStructure
from netex.models.sales_offer_package_refs_rel_structure import SalesOfferPackageRefsRelStructure
from netex.models.type_of_sales_offer_package_ref import TypeOfSalesOfferPackageRef

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
    limiting_rule_ref: List[LimitingRuleRef] = field(
        default_factory=list,
        metadata={
            "name": "LimitingRuleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 6,
            "sequential": True,
        }
    )
    discounting_rule_ref: List[DiscountingRuleRef] = field(
        default_factory=list,
        metadata={
            "name": "DiscountingRuleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    pricing_rule_ref: Optional[PricingRuleRef] = field(
        default=None,
        metadata={
            "name": "PricingRuleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    price_groups: Optional[PriceGroupsRelStructure] = field(
        default=None,
        metadata={
            "name": "priceGroups",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_tables: Optional[FareTablesRelStructure] = field(
        default=None,
        metadata={
            "name": "fareTables",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_sales_offer_package_ref: Optional[TypeOfSalesOfferPackageRef] = field(
        default=None,
        metadata={
            "name": "TypeOfSalesOfferPackageRef",
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
    validity_parameter_assignments: Optional[GenericParameterAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "validityParameterAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    distribution_assignments: Optional[DistributionAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "distributionAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    rounding_ref: Optional[RoundingRef] = field(
        default=None,
        metadata={
            "name": "RoundingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    prices: Optional[SalesOfferPackagePricesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sales_offer_package_elements: Optional[SalesOfferPackageElementsRelStructure] = field(
        default=None,
        metadata={
            "name": "salesOfferPackageElements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    members: Optional[SalesOfferPackageRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
