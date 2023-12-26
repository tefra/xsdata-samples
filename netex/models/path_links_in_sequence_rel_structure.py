from dataclasses import dataclass, field
from typing import List
from .path_link_in_sequence import PathLinkInSequence
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PathLinksInSequenceRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "pathLinksInSequence_RelStructure"

    path_link_in_sequence: List[PathLinkInSequence] = field(
        default_factory=list,
        metadata={
            "name": "PathLinkInSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
