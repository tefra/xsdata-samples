from dataclasses import dataclass, field
from typing import Optional
from netex.models.cell_versioned_child_structure import PriceableObjectVersionStructure
from netex.models.condition_summary import ConditionSummary
from netex.models.distribution_assignments_rel_structure import DistributionAssignmentsRelStructure
from netex.models.generic_parameter_assignment_version_structure import GenericParameterAssignmentsRelStructure
from netex.models.group_of_sales_offer_package_refs_rel_structure import GroupOfSalesOfferPackageRefsRelStructure
from netex.models.group_of_sales_offer_packages_ref import GroupOfSalesOfferPackagesRef
from netex.models.private_code import PrivateCode
from netex.models.rounding_ref import RoundingRef
from netex.models.sales_offer_package_elements_rel_structure import SalesOfferPackageElementsRelStructure
from netex.models.sales_offer_package_prices_rel_structure import SalesOfferPackagePricesRelStructure
from netex.models.sales_offer_package_substitutions_rel_structure import SalesOfferPackageSubstitutionsRelStructure
from netex.models.type_of_sales_offer_package_ref import TypeOfSalesOfferPackageRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SalesOfferPackageVersionStructure(PriceableObjectVersionStructure):
    class Meta:
        name = "SalesOfferPackage_VersionStructure"

    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
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
    group_of_sales_offer_packages_ref: Optional[GroupOfSalesOfferPackagesRef] = field(
        default=None,
        metadata={
            "name": "GroupOfSalesOfferPackagesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    groups_of_sale_offer_packages: Optional[GroupOfSalesOfferPackageRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "groupsOfSaleOfferPackages",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sales_offer_package_substitutions: Optional[SalesOfferPackageSubstitutionsRelStructure] = field(
        default=None,
        metadata={
            "name": "salesOfferPackageSubstitutions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
