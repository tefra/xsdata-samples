from dataclasses import dataclass
from .sales_offer_package_price_ref_structure import (
    SalesOfferPackagePriceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SalesOfferPackagePriceRef(SalesOfferPackagePriceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
