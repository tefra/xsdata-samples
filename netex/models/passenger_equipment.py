from __future__ import annotations

from dataclasses import dataclass

from .passenger_equipment_version_structure import (
    PassengerEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PassengerEquipment(PassengerEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
