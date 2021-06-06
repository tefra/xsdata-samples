from dataclasses import dataclass
from .point_in_sequence_ref_structure import PointInSequenceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointInSequenceRef(PointInSequenceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
