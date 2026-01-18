from __future__ import annotations

from dataclasses import dataclass

from .travelator_equipment_version_structure import (
    TravelatorEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TravelatorEquipment(TravelatorEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
