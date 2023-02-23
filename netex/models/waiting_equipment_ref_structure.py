from dataclasses import dataclass
from .site_equipment_ref_structure import SiteEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class WaitingEquipmentRefStructure(SiteEquipmentRefStructure):
    pass
