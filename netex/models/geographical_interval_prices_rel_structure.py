from dataclasses import dataclass, field
from typing import List, Union
from .cell_ref_1 import CellRef1
from .geographical_interval_price_ref import GeographicalIntervalPriceRef
from .geographical_interval_price_versioned_child_structure import (
    GeographicalIntervalPriceVersionedChildStructure,
)
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GeographicalIntervalPricesRelStructure(
    StrictContainmentAggregationStructure
):
    class Meta:
        name = "geographicalIntervalPrices_RelStructure"

    geographical_interval_price_ref_or_geographical_interval_price_or_cell_ref: List[
        Union[
            GeographicalIntervalPriceRef,
            GeographicalIntervalPriceVersionedChildStructure,
            CellRef1,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "GeographicalIntervalPriceRef",
                    "type": GeographicalIntervalPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalIntervalPrice",
                    "type": GeographicalIntervalPriceVersionedChildStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CellRef",
                    "type": CellRef1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
