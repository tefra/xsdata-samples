from __future__ import annotations

from dataclasses import dataclass

from .sign_equipment_version_structure import SignEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SignEquipment(SignEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
