from dataclasses import dataclass
from .trip_ref_structure import TripRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TripRef(TripRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
