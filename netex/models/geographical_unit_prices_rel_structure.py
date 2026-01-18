from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import ForwardRef

from .cell_ref import CellRef
from .fare_price_versioned_child_structure import (
    FarePriceVersionedChildStructure,
)
from .geographical_unit_price_ref import GeographicalUnitPriceRef
from .geographical_unit_ref import GeographicalUnitRef
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GeographicalUnitPricesRelStructure(
    StrictContainmentAggregationStructure
):
    class Meta:
        name = "geographicalUnitPrices_RelStructure"

    geographical_unit_price_ref_or_geographical_unit_price_or_cell_ref: Iterable[
        GeographicalUnitPriceRef
        | GeographicalUnitPriceVersionedChildStructure
        | CellRef
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "GeographicalUnitPriceRef",
                    "type": GeographicalUnitPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalUnitPrice",
                    "type": ForwardRef(
                        "GeographicalUnitPriceVersionedChildStructure"
                    ),
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


@dataclass(kw_only=True)
class GeographicalUnitPriceVersionedChildStructure(
    FarePriceVersionedChildStructure
):
    class Meta:
        name = "GeographicalUnitPrice_VersionedChildStructure"

    geographical_unit_ref: None | GeographicalUnitRef = field(
        default=None,
        metadata={
            "name": "GeographicalUnitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    prices: None | GeographicalUnitPricesRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
