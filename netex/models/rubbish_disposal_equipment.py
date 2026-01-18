from __future__ import annotations

from dataclasses import dataclass

from .rubbish_disposal_equipment_version_structure import (
    RubbishDisposalEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RubbishDisposalEquipment(RubbishDisposalEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
