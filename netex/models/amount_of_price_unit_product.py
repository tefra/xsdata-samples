from dataclasses import dataclass
from .amount_of_price_unit_product_version_structure import (
    AmountOfPriceUnitProductVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AmountOfPriceUnitProduct(AmountOfPriceUnitProductVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
