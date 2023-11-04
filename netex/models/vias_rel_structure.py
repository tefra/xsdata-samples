from dataclasses import dataclass, field
from typing import List, Union
from .empty_type_2 import EmptyType2
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure
from .via_versioned_child_structure import ViaVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ViasRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "vias_RelStructure"

    none_or_via: List[Union[ViaVersionedChildStructure, EmptyType2]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "None",
                    "type": EmptyType2,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Via",
                    "type": ViaVersionedChildStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
