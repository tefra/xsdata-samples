from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from .place_equipment_version_structure import PlaceEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleChargingEquipmentVersionStructure(PlaceEquipmentVersionStructure):
    class Meta:
        name = "VehicleChargingEquipment_VersionStructure"

    free_recharging: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FreeRecharging",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    reservation_required: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReservationRequired",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    reservation_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReservationUrl",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_power: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaximumPower",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    grid_voltage: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "GridVoltage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
