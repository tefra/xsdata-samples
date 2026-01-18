from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from .place_equipment_version_structure import PlaceEquipmentVersionStructure
from .type_of_battery_chemistry_ref import TypeOfBatteryChemistryRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class BatteryEquipmentVersionStructure(PlaceEquipmentVersionStructure):
    class Meta:
        name = "BatteryEquipment_VersionStructure"

    battery_capacity: None | Decimal = field(
        default=None,
        metadata={
            "name": "BatteryCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    battery_usable_capacity: None | Decimal = field(
        default=None,
        metadata={
            "name": "BatteryUsableCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    nominal_voltage: None | Decimal = field(
        default=None,
        metadata={
            "name": "NominalVoltage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_charging_power: None | Decimal = field(
        default=None,
        metadata={
            "name": "MaximumChargingPower",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_battery_chemistry_ref: None | TypeOfBatteryChemistryRef = field(
        default=None,
        metadata={
            "name": "TypeOfBatteryChemistryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
