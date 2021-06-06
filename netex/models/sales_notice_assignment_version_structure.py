from dataclasses import dataclass, field
from typing import Optional
from .country_ref import CountryRef
from .group_of_sales_offer_packages_ref import GroupOfSalesOfferPackagesRef
from .notice_assignment_version_structure import NoticeAssignmentVersionStructure
from .sales_offer_package_ref import SalesOfferPackageRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SalesNoticeAssignmentVersionStructure(NoticeAssignmentVersionStructure):
    class Meta:
        name = "SalesNoticeAssignment_VersionStructure"

    country_ref: Optional[CountryRef] = field(
        default=None,
        metadata={
            "name": "CountryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sales_offer_package_ref: Optional[SalesOfferPackageRef] = field(
        default=None,
        metadata={
            "name": "SalesOfferPackageRef",
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
