from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from .amount_of_price_unit_enumeration import AmountOfPriceUnitEnumeration
from .fare_product_version_structure import FareProductVersionStructure
from .price_unit_ref import PriceUnitRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AmountOfPriceUnitProductVersionStructure(FareProductVersionStructure):
    class Meta:
        name = "AmountOfPriceUnitProduct_VersionStructure"

    product_type: Optional[AmountOfPriceUnitEnumeration] = field(
        default=None,
        metadata={
            "name": "ProductType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    price_unit_ref: Optional[PriceUnitRef] = field(
        default=None,
        metadata={
            "name": "PriceUnitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
