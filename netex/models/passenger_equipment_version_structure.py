from dataclasses import dataclass, field
from typing import Optional

from .installed_equipment_version_structure import (
    InstalledEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PassengerEquipmentVersionStructure(InstalledEquipmentVersionStructure):
    class Meta:
        name = "PassengerEquipment_VersionStructure"

    fixed: bool | None = field(
        default=None,
        metadata={
            "name": "Fixed",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
