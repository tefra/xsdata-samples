from dataclasses import dataclass

from .controllable_element_in_sequence_versioned_child_structure import (
    ControllableElementInSequenceVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ControllableElementInSequence(
    ControllableElementInSequenceVersionedChildStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
