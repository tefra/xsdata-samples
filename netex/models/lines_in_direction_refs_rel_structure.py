from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .line_in_direction_ref import LineInDirectionRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LinesInDirectionRefsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "linesInDirectionRefs_RelStructure"

    line_in_direction_ref: Iterable[LineInDirectionRef] = field(
        default_factory=list,
        metadata={
            "name": "LineInDirectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
