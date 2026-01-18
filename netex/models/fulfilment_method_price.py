from __future__ import annotations

from dataclasses import dataclass

from .fulfilment_method_price_versioned_child_structure import (
    FulfilmentMethodPriceVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FulfilmentMethodPrice(FulfilmentMethodPriceVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
