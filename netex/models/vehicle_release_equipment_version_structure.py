from __future__ import annotations

from dataclasses import dataclass, field

from .installed_equipment_version_structure import (
    InstalledEquipmentVersionStructure,
)
from .locking_mechanism_enumeration import LockingMechanismEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleReleaseEquipmentVersionStructure(
    InstalledEquipmentVersionStructure
):
    class Meta:
        name = "VehicleReleaseEquipment_VersionStructure"

    remote_control: bool | None = field(
        default=None,
        metadata={
            "name": "RemoteControl",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    local_control: bool | None = field(
        default=None,
        metadata={
            "name": "LocalControl",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    locking_mechanism: LockingMechanismEnumeration | None = field(
        default=None,
        metadata={
            "name": "LockingMechanism",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
