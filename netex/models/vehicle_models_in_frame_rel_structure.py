from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .vehicle_model import VehicleModel

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleModelsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "vehicleModelsInFrame_RelStructure"

    vehicle_model: List[VehicleModel] = field(
        default_factory=list,
        metadata={
            "name": "VehicleModel",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
