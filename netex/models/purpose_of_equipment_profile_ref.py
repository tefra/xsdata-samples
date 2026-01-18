from __future__ import annotations

from dataclasses import dataclass

from .purpose_of_equipment_profile_ref_structure import (
    PurposeOfEquipmentProfileRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PurposeOfEquipmentProfileRef(PurposeOfEquipmentProfileRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
