from dataclasses import dataclass
from netex.models.sale_discount_right_version_structure import SaleDiscountRightVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SaleDiscountRight(SaleDiscountRightVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
