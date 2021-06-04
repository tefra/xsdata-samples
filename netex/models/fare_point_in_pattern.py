from dataclasses import dataclass
from netex.models.fare_point_in_pattern_versioned_child_structure import FarePointInPatternVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FarePointInPattern(FarePointInPatternVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
