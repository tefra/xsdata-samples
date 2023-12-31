from dataclasses import dataclass
from .battery_equipment_ref_structure import BatteryEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class BatteryEquipmentRef(BatteryEquipmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
