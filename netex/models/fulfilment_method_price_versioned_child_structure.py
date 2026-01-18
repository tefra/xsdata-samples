from __future__ import annotations

from dataclasses import dataclass, field

from .fare_price_versioned_child_structure import (
    FarePriceVersionedChildStructure,
)
from .fulfilment_method_ref import FulfilmentMethodRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FulfilmentMethodPriceVersionedChildStructure(
    FarePriceVersionedChildStructure
):
    class Meta:
        name = "FulfilmentMethodPrice_VersionedChildStructure"

    fulfilment_method_ref: None | FulfilmentMethodRef = field(
        default=None,
        metadata={
            "name": "FulfilmentMethodRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
