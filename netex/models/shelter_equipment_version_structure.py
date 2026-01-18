from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from .waiting_equipment_version_structure import (
    WaitingEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ShelterEquipmentVersionStructure(WaitingEquipmentVersionStructure):
    class Meta:
        name = "ShelterEquipment_VersionStructure"

    enclosed: bool | None = field(
        default=None,
        metadata={
            "name": "Enclosed",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    distance_from_nearest_kerb: Decimal | None = field(
        default=None,
        metadata={
            "name": "DistanceFromNearestKerb",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
