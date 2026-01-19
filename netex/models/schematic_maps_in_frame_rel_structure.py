from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .schematic_map import SchematicMap

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SchematicMapsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "schematicMapsInFrame_RelStructure"

    schematic_map: Sequence[SchematicMap] = field(
        default_factory=list,
        metadata={
            "name": "SchematicMap",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
