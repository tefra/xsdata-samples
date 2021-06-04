from dataclasses import dataclass, field
from typing import List
from netex.models.strict_containment_aggregation_structure import StrictContainmentAggregationStructure
from netex.models.vehicle_journey_run_time import VehicleJourneyRunTime

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleJourneyRunTimesRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "vehicleJourneyRunTimes_RelStructure"

    vehicle_journey_run_time: List[VehicleJourneyRunTime] = field(
        default_factory=list,
        metadata={
            "name": "VehicleJourneyRunTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
