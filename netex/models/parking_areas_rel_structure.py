from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .parking_area import ParkingArea
from .parking_area_ref import ParkingAreaRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ParkingAreasRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "parkingAreas_RelStructure"

    parking_area_ref: List[ParkingAreaRef] = field(
        default_factory=list,
        metadata={
            "name": "ParkingAreaRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_area: List[ParkingArea] = field(
        default_factory=list,
        metadata={
            "name": "ParkingArea",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
