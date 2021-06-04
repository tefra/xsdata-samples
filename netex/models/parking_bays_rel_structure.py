from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.parking_bay import ParkingBay
from netex.models.parking_bay_ref import ParkingBayRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ParkingBaysRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "parkingBays_RelStructure"

    parking_bay_ref: List[ParkingBayRef] = field(
        default_factory=list,
        metadata={
            "name": "ParkingBayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_bay: List[ParkingBay] = field(
        default_factory=list,
        metadata={
            "name": "ParkingBay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
