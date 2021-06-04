from dataclasses import dataclass
from netex.models.stair_flight_versioned_child_structure import StairFlightVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class StairFlight(StairFlightVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
