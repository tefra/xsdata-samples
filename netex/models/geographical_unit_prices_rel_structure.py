from dataclasses import dataclass, field
from typing import List, Optional, Type, Union

from .cell_ref_1 import CellRef1
from .fare_price_versioned_child_structure import (
    FarePriceVersionedChildStructure,
)
from .geographical_unit_price_ref import GeographicalUnitPriceRef
from .geographical_unit_ref import GeographicalUnitRef
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GeographicalUnitPricesRelStructure(
    StrictContainmentAggregationStructure
):
    class Meta:
        name = "geographicalUnitPrices_RelStructure"

    geographical_unit_price_ref_or_geographical_unit_price_or_cell_ref: List[
        Union[
            GeographicalUnitPriceRef,
            "GeographicalUnitPriceVersionedChildStructure",
            CellRef1,
        ]
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
                    "type": Type[
                        "GeographicalUnitPriceVersionedChildStructure"
                    ],
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


@dataclass
class GeographicalUnitPriceVersionedChildStructure(
    FarePriceVersionedChildStructure
):
    class Meta:
        name = "GeographicalUnitPrice_VersionedChildStructure"

    geographical_unit_ref: Optional[GeographicalUnitRef] = field(
        default=None,
        metadata={
            "name": "GeographicalUnitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    prices: Optional[GeographicalUnitPricesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
