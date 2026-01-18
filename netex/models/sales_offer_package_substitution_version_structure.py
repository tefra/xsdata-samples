from dataclasses import dataclass, field

from .assignment_version_structure_1 import AssignmentVersionStructure1
from .sales_offer_package_ref import SalesOfferPackageRef
from .sales_offer_package_ref_structure import SalesOfferPackageRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SalesOfferPackageSubstitutionVersionStructure(
    AssignmentVersionStructure1
):
    class Meta:
        name = "SalesOfferPackageSubstitution_VersionStructure"

    sales_offer_package_ref: SalesOfferPackageRef | None = field(
        default=None,
        metadata={
            "name": "SalesOfferPackageRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    with_sales_offer_package_ref: SalesOfferPackageRefStructure | None = field(
        default=None,
        metadata={
            "name": "WithSalesOfferPackageRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
