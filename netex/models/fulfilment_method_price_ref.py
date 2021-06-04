from dataclasses import dataclass
from netex.models.fulfilment_method_price_ref_structure import FulfilmentMethodPriceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FulfilmentMethodPriceRef(FulfilmentMethodPriceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
