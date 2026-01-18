from __future__ import annotations

from dataclasses import dataclass

from .activated_equipment_ref_structure import ActivatedEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ActivatedEquipmentRef(ActivatedEquipmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
