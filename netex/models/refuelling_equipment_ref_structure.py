from __future__ import annotations

from dataclasses import dataclass

from .equipment_ref_structure import EquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RefuellingEquipmentRefStructure(EquipmentRefStructure):
    pass
