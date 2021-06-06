from dataclasses import dataclass, field
from typing import List
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure
from .vehicle_journey_headway import VehicleJourneyHeadway

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleJourneyHeadwaysRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "vehicleJourneyHeadways_RelStructure"

    vehicle_journey_headway: List[VehicleJourneyHeadway] = field(
        default_factory=list,
        metadata={
            "name": "VehicleJourneyHeadway",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
