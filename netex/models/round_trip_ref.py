from dataclasses import dataclass
from .round_trip_ref_structure import RoundTripRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RoundTripRef(RoundTripRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
