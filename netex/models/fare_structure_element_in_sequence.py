from dataclasses import dataclass
from netex.models.fare_structure_element_in_sequence_versioned_child_structure import FareStructureElementInSequenceVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareStructureElementInSequence(FareStructureElementInSequenceVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
