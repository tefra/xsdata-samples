from collections.abc import Iterable
from dataclasses import dataclass, field

from .group_of_link_sequences import GroupOfLinkSequences
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupOfLinkSequencesRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "groupOfLinkSequences_RelStructure"

    group_of_link_sequences: Iterable[GroupOfLinkSequences] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfLinkSequences",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
