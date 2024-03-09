from dataclasses import dataclass, field
from typing import List, Union

from .charging_equipment_profile_ref import ChargingEquipmentProfileRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .vehicle_equipment_profile_ref import VehicleEquipmentProfileRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleEquipmentProfileRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "vehicleEquipmentProfileRefs_RelStructure"

    vehicle_equipment_profile_ref: List[
        Union[ChargingEquipmentProfileRef, VehicleEquipmentProfileRef]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ChargingEquipmentProfileRef",
                    "type": ChargingEquipmentProfileRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleEquipmentProfileRef",
                    "type": VehicleEquipmentProfileRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
