from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from .place_equipment_version_structure import PlaceEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleChargingEquipmentVersionStructure(PlaceEquipmentVersionStructure):
    class Meta:
        name = "VehicleChargingEquipment_VersionStructure"

    free_recharging: None | bool = field(
        default=None,
        metadata={
            "name": "FreeRecharging",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    reservation_required: None | bool = field(
        default=None,
        metadata={
            "name": "ReservationRequired",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    reservation_url: None | str = field(
        default=None,
        metadata={
            "name": "ReservationUrl",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_power: None | Decimal = field(
        default=None,
        metadata={
            "name": "MaximumPower",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    grid_voltage: None | Decimal = field(
        default=None,
        metadata={
            "name": "GridVoltage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
