from dataclasses import dataclass, field
from typing import List
from .controllable_element_in_sequence import ControllableElementInSequence
from .fare_structure_element_in_sequence import FareStructureElementInSequence
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareStructureElementsInSequenceRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "fareStructureElementsInSequence_RelStructure"

    fare_structure_element_in_sequence: List[FareStructureElementInSequence] = field(
        default_factory=list,
        metadata={
            "name": "FareStructureElementInSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    controllable_element_in_sequence: List[ControllableElementInSequence] = field(
        default_factory=list,
        metadata={
            "name": "ControllableElementInSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
