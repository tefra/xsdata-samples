from dataclasses import dataclass
from .help_point_equipment_version_structure import (
    HelpPointEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class HelpPointEquipment(HelpPointEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
