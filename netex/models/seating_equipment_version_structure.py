from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from .waiting_equipment_version_structure import (
    WaitingEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SeatingEquipmentVersionStructure(WaitingEquipmentVersionStructure):
    class Meta:
        name = "SeatingEquipment_VersionStructure"

    arm_rest: None | bool = field(
        default=None,
        metadata={
            "name": "ArmRest",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    back_rest: None | bool = field(
        default=None,
        metadata={
            "name": "BackRest",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    seat_height: None | Decimal = field(
        default=None,
        metadata={
            "name": "SeatHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
