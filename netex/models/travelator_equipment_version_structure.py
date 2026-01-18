from dataclasses import dataclass, field
from decimal import Decimal

from .access_equipment_version_structure import AccessEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TravelatorEquipmentVersionStructure(AccessEquipmentVersionStructure):
    class Meta:
        name = "TravelatorEquipment_VersionStructure"

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
    speed: Decimal | None = field(
        default=None,
        metadata={
            "name": "Speed",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    length: Decimal | None = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    gradient: Decimal | None = field(
        default=None,
        metadata={
            "name": "Gradient",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    integrates_an_escalator_part: bool | None = field(
        default=None,
        metadata={
            "name": "IntegratesAnEscalatorPart",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
