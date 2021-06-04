from dataclasses import dataclass, field
from typing import List
from netex.models.parking_properties import ParkingProperties
from netex.models.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ParkingPropertiesRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "parkingProperties_RelStructure"

    parking_properties: List[ParkingProperties] = field(
        default_factory=list,
        metadata={
            "name": "ParkingProperties",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
