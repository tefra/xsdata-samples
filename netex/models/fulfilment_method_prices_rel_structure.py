from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .cell_ref import CellRef
from .fulfilment_method_price_ref import FulfilmentMethodPriceRef
from .fulfilment_method_price_versioned_child_structure import (
    FulfilmentMethodPriceVersionedChildStructure,
)
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FulfilmentMethodPricesRelStructure(
    StrictContainmentAggregationStructure
):
    class Meta:
        name = "fulfilmentMethodPrices_RelStructure"

    fulfilment_method_price_ref_or_fulfilment_method_price_or_cell_ref: Sequence[
        FulfilmentMethodPriceRef
        | FulfilmentMethodPriceVersionedChildStructure
        | CellRef
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FulfilmentMethodPriceRef",
                    "type": FulfilmentMethodPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FulfilmentMethodPrice",
                    "type": FulfilmentMethodPriceVersionedChildStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CellRef",
                    "type": CellRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
