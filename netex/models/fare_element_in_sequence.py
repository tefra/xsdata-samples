from dataclasses import dataclass

from .fare_element_in_sequence_versioned_child_structure import (
    FareElementInSequenceVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareElementInSequence(FareElementInSequenceVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
