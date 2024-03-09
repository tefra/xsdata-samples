from dataclasses import dataclass

from .usage_discount_right_version_structure import (
    UsageDiscountRightVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class UsageDiscountRight(UsageDiscountRightVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
