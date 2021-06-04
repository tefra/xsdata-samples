from dataclasses import dataclass, field
from typing import Optional
from netex.models.fare_price_versioned_child_structure import FarePriceVersionedChildStructure
from netex.models.fulfilment_method_ref import FulfilmentMethodRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FulfilmentMethodPriceVersionedChildStructure(FarePriceVersionedChildStructure):
    class Meta:
        name = "FulfilmentMethodPrice_VersionedChildStructure"

    fulfilment_method_ref: Optional[FulfilmentMethodRef] = field(
        default=None,
        metadata={
            "name": "FulfilmentMethodRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
