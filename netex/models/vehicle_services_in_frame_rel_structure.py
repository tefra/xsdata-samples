from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .vehicle_service import VehicleService

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleServicesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "vehicleServicesInFrame_RelStructure"

    vehicle_service: List[VehicleService] = field(
        default_factory=list,
        metadata={
            "name": "VehicleService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
