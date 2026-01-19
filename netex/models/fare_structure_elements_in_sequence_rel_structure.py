from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .controllable_element_in_sequence import ControllableElementInSequence
from .fare_structure_element_in_sequence import FareStructureElementInSequence
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareStructureElementsInSequenceRelStructure(
    StrictContainmentAggregationStructure
):
    class Meta:
        name = "fareStructureElementsInSequence_RelStructure"

    fare_structure_element_in_sequence_or_controllable_element_in_sequence: Sequence[
        FareStructureElementInSequence | ControllableElementInSequence
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FareStructureElementInSequence",
                    "type": FareStructureElementInSequence,
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
