from __future__ import annotations

from dataclasses import dataclass

from .lift_equipment_version_structure import LiftEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LiftEquipment(LiftEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
