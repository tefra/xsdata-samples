from __future__ import annotations

from dataclasses import dataclass

from .site_equipment_version_structure import SiteEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SiteEquipment(SiteEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
