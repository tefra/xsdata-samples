from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from .place_equipment_version_structure import PlaceEquipmentVersionStructure
from .type_of_battery_chemistry_ref import TypeOfBatteryChemistryRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class BatteryEquipmentVersionStructure(PlaceEquipmentVersionStructure):
    class Meta:
        name = "BatteryEquipment_VersionStructure"

    battery_capacity: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "BatteryCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    battery_usable_capacity: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "BatteryUsableCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    nominal_voltage: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "NominalVoltage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_charging_power: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaximumChargingPower",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_battery_chemistry_ref: Optional[TypeOfBatteryChemistryRef] = field(
        default=None,
        metadata={
            "name": "TypeOfBatteryChemistryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
