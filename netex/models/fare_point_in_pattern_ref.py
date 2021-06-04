from dataclasses import dataclass
from netex.models.fare_point_in_pattern_ref_structure import FarePointInPatternRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FarePointInPatternRef(FarePointInPatternRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
