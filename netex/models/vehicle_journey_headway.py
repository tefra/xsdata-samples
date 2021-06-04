from dataclasses import dataclass
from netex.models.vehicle_journey_headway_versioned_child_structure import VehicleJourneyHeadwayVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleJourneyHeadway(VehicleJourneyHeadwayVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
