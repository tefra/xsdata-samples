from __future__ import annotations

from dataclasses import dataclass

from .passenger_equipment_ref_structure import PassengerEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RubbishDisposalEquipmentRefStructure(PassengerEquipmentRefStructure):
    pass
