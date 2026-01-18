from __future__ import annotations

from dataclasses import dataclass, field

from .stair_equipment_version_structure import StairEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class EscalatorEquipmentVersionStructure(StairEquipmentVersionStructure):
    class Meta:
        name = "EscalatorEquipment_VersionStructure"

    tactile_actuators: bool | None = field(
        default=None,
        metadata={
            "name": "TactileActuators",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    energy_saving: bool | None = field(
        default=None,
        metadata={
            "name": "EnergySaving",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    dogs_must_be_carried: bool | None = field(
        default=None,
        metadata={
            "name": "DogsMustBeCarried",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    escalator_with_landing: bool | None = field(
        default=None,
        metadata={
            "name": "EscalatorWithLanding",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    monitoring_remote_control: bool | None = field(
        default=None,
        metadata={
            "name": "MonitoringRemoteControl",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
