from dataclasses import dataclass, field
from typing import List
from netex.models.controllable_element_in_sequence import ControllableElementInSequence
from netex.models.controllable_element_in_sequence_ref import ControllableElementInSequenceRef
from netex.models.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ControllableElementsInSequenceRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "controllableElementsInSequence_RelStructure"

    controllable_element_in_sequence_ref: List[ControllableElementInSequenceRef] = field(
        default_factory=list,
        metadata={
            "name": "ControllableElementInSequenceRef",
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
