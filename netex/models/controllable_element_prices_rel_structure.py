from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .cell_ref import CellRef
from .controllable_element_price import ControllableElementPrice
from .controllable_element_price_ref import ControllableElementPriceRef
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ControllableElementPricesRelStructure(
    StrictContainmentAggregationStructure
):
    class Meta:
        name = "controllableElementPrices_RelStructure"

    controllable_element_price_ref_or_cell_ref_or_controllable_element_price: Iterable[
        ControllableElementPriceRef | CellRef | ControllableElementPrice
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ControllableElementPriceRef",
                    "type": ControllableElementPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CellRef",
                    "type": CellRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ControllableElementPrice",
                    "type": ControllableElementPrice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
