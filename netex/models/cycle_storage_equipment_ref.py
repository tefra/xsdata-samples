from dataclasses import dataclass
from .cycle_storage_equipment_ref_structure import (
    CycleStorageEquipmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CycleStorageEquipmentRef(CycleStorageEquipmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
