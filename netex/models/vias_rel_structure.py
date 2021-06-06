from dataclasses import dataclass, field
from typing import List, Optional
from .empty_type_2 import EmptyType2
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure
from .via_versioned_child_structure import ViaVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ViasRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "vias_RelStructure"

    none_value: Optional[EmptyType2] = field(
        default=None,
        metadata={
            "name": "None",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    via: List[ViaVersionedChildStructure] = field(
        default_factory=list,
        metadata={
            "name": "Via",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
