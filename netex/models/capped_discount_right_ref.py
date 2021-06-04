from dataclasses import dataclass
from netex.models.capped_discount_right_ref_structure import CappedDiscountRightRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CappedDiscountRightRef(CappedDiscountRightRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
