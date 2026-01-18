from __future__ import annotations

from dataclasses import dataclass, field

from .condition_summary import ConditionSummary
from .distribution_assignments_rel_structure import (
    DistributionAssignmentsRelStructure,
)
from .generic_parameter_assignments_rel_structure import (
    GenericParameterAssignmentsRelStructure,
)
from .group_of_sales_offer_package_refs_rel_structure import (
    GroupOfSalesOfferPackageRefsRelStructure,
)
from .group_of_sales_offer_packages_ref import GroupOfSalesOfferPackagesRef
from .priceable_object_version_structure import PriceableObjectVersionStructure
from .private_code import PrivateCode
from .rounding_ref import RoundingRef
from .sales_offer_package_elements_rel_structure import (
    SalesOfferPackageElementsRelStructure,
)
from .sales_offer_package_prices_rel_structure import (
    SalesOfferPackagePricesRelStructure,
)
from .sales_offer_package_substitutions_rel_structure import (
    SalesOfferPackageSubstitutionsRelStructure,
)
from .type_of_sales_offer_package_ref import TypeOfSalesOfferPackageRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SalesOfferPackageVersionStructure(PriceableObjectVersionStructure):
    class Meta:
        name = "SalesOfferPackage_VersionStructure"

    private_code: PrivateCode | None = field(
        default=None,
        metadata={
            "name": "PrivateCode",
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
    group_of_sales_offer_packages_ref_or_groups_of_sale_offer_packages: (
        GroupOfSalesOfferPackagesRef
        | GroupOfSalesOfferPackageRefsRelStructure
        | None
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "GroupOfSalesOfferPackagesRef",
                    "type": GroupOfSalesOfferPackagesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "groupsOfSaleOfferPackages",
                    "type": GroupOfSalesOfferPackageRefsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    sales_offer_package_substitutions: (
        SalesOfferPackageSubstitutionsRelStructure | None
    ) = field(
        default=None,
        metadata={
            "name": "salesOfferPackageSubstitutions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
