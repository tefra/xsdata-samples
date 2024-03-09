from dataclasses import dataclass, field
from typing import List, Union

from .charging_equipment_profile import ChargingEquipmentProfile
from .containment_aggregation_structure import ContainmentAggregationStructure
from .vehicle_equipment_profile import VehicleEquipmentProfile

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleEquipmenProfilesInFrameRelStructure(
    ContainmentAggregationStructure
):
    class Meta:
        name = "vehicleEquipmenProfilesInFrame_RelStructure"

    vehicle_equipment_profile_or_charging_equipment_profile: List[
        Union[VehicleEquipmentProfile, ChargingEquipmentProfile]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VehicleEquipmentProfile",
                    "type": VehicleEquipmentProfile,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ChargingEquipmentProfile",
                    "type": ChargingEquipmentProfile,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
