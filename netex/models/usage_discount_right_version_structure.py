from dataclasses import dataclass, field
from typing import Optional

from .fare_product_version_structure import FareProductVersionStructure
from .usage_discount_right_enumeration import UsageDiscountRightEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class UsageDiscountRightVersionStructure(FareProductVersionStructure):
    class Meta:
        name = "UsageDiscountRight_VersionStructure"

    product_type: Optional[UsageDiscountRightEnumeration] = field(
        default=None,
        metadata={
            "name": "ProductType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
