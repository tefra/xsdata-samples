from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .vehicle_stopping_place import VehicleStoppingPlace
from .vehicle_stopping_place_ref import VehicleStoppingPlaceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleStoppingPlacesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "vehicleStoppingPlaces_RelStructure"

    vehicle_stopping_place_ref: List[VehicleStoppingPlaceRef] = field(
        default_factory=list,
        metadata={
            "name": "VehicleStoppingPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_stopping_place: List[VehicleStoppingPlace] = field(
        default_factory=list,
        metadata={
            "name": "VehicleStoppingPlace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
