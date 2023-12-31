from dataclasses import dataclass
from .trip_pattern_ref_structure import TripPatternRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TripPatternTripRef(TripPatternRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
