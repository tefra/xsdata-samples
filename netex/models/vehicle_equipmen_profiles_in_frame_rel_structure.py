from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .vehicle_equipment_profile import VehicleEquipmentProfile

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleEquipmenProfilesInFrameRelStructure(
    ContainmentAggregationStructure
):
    class Meta:
        name = "vehicleEquipmenProfilesInFrame_RelStructure"

    vehicle_equipment_profile: List[VehicleEquipmentProfile] = field(
        default_factory=list,
        metadata={
            "name": "VehicleEquipmentProfile",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
