from dataclasses import dataclass
from netex.models.point_in_link_sequence_versioned_child_structure import PointInLinkSequenceVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointOnSection2(PointInLinkSequenceVersionedChildStructure):
    class Meta:
        name = "PointOnSection_"
        namespace = "http://www.netex.org.uk/netex"
