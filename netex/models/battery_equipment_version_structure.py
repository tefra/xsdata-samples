from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from .place_equipment_version_structure import PlaceEquipmentVersionStructure
from .type_of_battery_chemistry_ref import TypeOfBatteryChemistryRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class BatteryEquipmentVersionStructure(PlaceEquipmentVersionStructure):
    class Meta:
        name = "BatteryEquipment_VersionStructure"

    battery_capacity: Decimal | None = field(
        default=None,
        metadata={
            "name": "BatteryCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    battery_usable_capacity: Decimal | None = field(
        default=None,
        metadata={
            "name": "BatteryUsableCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    nominal_voltage: Decimal | None = field(
        default=None,
        metadata={
            "name": "NominalVoltage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_charging_power: Decimal | None = field(
        default=None,
        metadata={
            "name": "MaximumChargingPower",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_battery_chemistry_ref: TypeOfBatteryChemistryRef | None = field(
        default=None,
        metadata={
            "name": "TypeOfBatteryChemistryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
