from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .cell_ref import CellRef
from .series_constraint_price_ref import SeriesConstraintPriceRef
from .series_constraint_price_versioned_child_structure import (
    SeriesConstraintPriceVersionedChildStructure,
)
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SeriesConstraintPricesRelStructure(
    StrictContainmentAggregationStructure
):
    class Meta:
        name = "seriesConstraintPrices_RelStructure"

    series_constraint_price_ref_or_series_constraint_price_or_cell_ref: Iterable[
        SeriesConstraintPriceRef
        | SeriesConstraintPriceVersionedChildStructure
        | CellRef
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SeriesConstraintPriceRef",
                    "type": SeriesConstraintPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SeriesConstraintPrice",
                    "type": SeriesConstraintPriceVersionedChildStructure,
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
