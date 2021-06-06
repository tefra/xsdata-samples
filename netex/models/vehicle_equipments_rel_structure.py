from dataclasses import dataclass, field
from typing import List
from .access_vehicle_equipment import AccessVehicleEquipment
from .containment_aggregation_structure import ContainmentAggregationStructure
from .wheelchair_vehicle_equipment import WheelchairVehicleEquipment

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleEquipmentsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "vehicleEquipments_RelStructure"

    access_vehicle_equipment: List[AccessVehicleEquipment] = field(
        default_factory=list,
        metadata={
            "name": "AccessVehicleEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    wheelchair_vehicle_equipment: List[WheelchairVehicleEquipment] = field(
        default_factory=list,
        metadata={
            "name": "WheelchairVehicleEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
