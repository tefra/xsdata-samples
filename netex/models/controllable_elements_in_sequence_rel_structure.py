from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Union

from .controllable_element_in_sequence import ControllableElementInSequence
from .controllable_element_in_sequence_ref import (
    ControllableElementInSequenceRef,
)
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ControllableElementsInSequenceRelStructure(
    StrictContainmentAggregationStructure
):
    class Meta:
        name = "controllableElementsInSequence_RelStructure"

    controllable_element_in_sequence_ref_or_controllable_element_in_sequence: Iterable[
        Union[ControllableElementInSequenceRef, ControllableElementInSequence]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ControllableElementInSequenceRef",
                    "type": ControllableElementInSequenceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ControllableElementInSequence",
                    "type": ControllableElementInSequence,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
