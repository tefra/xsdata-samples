from dataclasses import dataclass

from .lift_call_equipment_version_structure import (
    LiftCallEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LiftCallEquipment(LiftCallEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
