from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.parking_capacity import ParkingCapacity
from netex.models.parking_capacity_ref import ParkingCapacityRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ParkingCapacitiesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "parkingCapacities_RelStructure"

    parking_capacity_ref: List[ParkingCapacityRef] = field(
        default_factory=list,
        metadata={
            "name": "ParkingCapacityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_capacity: List[ParkingCapacity] = field(
        default_factory=list,
        metadata={
            "name": "ParkingCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
