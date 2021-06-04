from dataclasses import dataclass
from netex.models.place_in_sequence_versioned_child_structure import PlaceInSequenceVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PlaceInSequence(PlaceInSequenceVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
