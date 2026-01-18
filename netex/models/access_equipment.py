from __future__ import annotations

from dataclasses import dataclass

from .access_equipment_version_structure import AccessEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccessEquipment(AccessEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
