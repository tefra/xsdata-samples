from dataclasses import dataclass
from netex.models.usage_discount_right_ref_structure import UsageDiscountRightRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class UsageDiscountRightRef(UsageDiscountRightRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
