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

    parking_area_ref_or_parking_area: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ParkingAreaRef",
                    "type": ParkingAreaRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingArea",
                    "type": ParkingArea,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
