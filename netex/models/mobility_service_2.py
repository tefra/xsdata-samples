from dataclasses import dataclass

from .equipment_version_structure import EquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class MobilityService2(EquipmentVersionStructure):
    class Meta:
        name = "MobilityService_"
        namespace = "http://www.netex.org.uk/netex"
