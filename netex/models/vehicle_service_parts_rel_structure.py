from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.vehicle_service_part import VehicleServicePart
from netex.models.vehicle_service_part_ref import VehicleServicePartRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleServicePartsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "vehicleServiceParts_RelStructure"

    vehicle_service_part_ref: List[VehicleServicePartRef] = field(
        default_factory=list,
        metadata={
            "name": "VehicleServicePartRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_service_part: List[VehicleServicePart] = field(
        default_factory=list,
        metadata={
            "name": "VehicleServicePart",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
