from __future__ import annotations

from dataclasses import dataclass

from .access_equipment_ref_structure import AccessEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PlaceLightingEquipmentRefStructure(AccessEquipmentRefStructure):
    pass
