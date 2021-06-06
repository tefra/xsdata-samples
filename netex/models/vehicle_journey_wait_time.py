from dataclasses import dataclass
from .vehicle_journey_wait_time_versioned_child_structure import VehicleJourneyWaitTimeVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleJourneyWaitTime(VehicleJourneyWaitTimeVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
