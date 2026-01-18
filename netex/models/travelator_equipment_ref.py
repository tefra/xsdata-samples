from __future__ import annotations

from dataclasses import dataclass

from .travelator_equipment_ref_structure import TravelatorEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TravelatorEquipmentRef(TravelatorEquipmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
