from dataclasses import dataclass, field
from typing import List

from .cell_ref import CellRef
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CellRefsRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "cellRefs_RelStructure"

    cell_ref: List[CellRef] = field(
        default_factory=list,
        metadata={
            "name": "CellRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
