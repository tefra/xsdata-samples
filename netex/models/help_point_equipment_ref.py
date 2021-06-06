from dataclasses import dataclass
from .help_point_equipment_ref_structure import HelpPointEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class HelpPointEquipmentRef(HelpPointEquipmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
