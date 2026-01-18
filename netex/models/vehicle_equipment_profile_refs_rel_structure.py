from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .charging_equipment_profile_ref import ChargingEquipmentProfileRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .vehicle_equipment_profile_ref import VehicleEquipmentProfileRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleEquipmentProfileRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "vehicleEquipmentProfileRefs_RelStructure"

    vehicle_equipment_profile_ref: Iterable[
        ChargingEquipmentProfileRef | VehicleEquipmentProfileRef
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
