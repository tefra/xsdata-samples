from __future__ import annotations

from dataclasses import dataclass

from .passenger_information_equipment_ref_structure import (
    PassengerInformationEquipmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PassengerInformationEquipmentRef(
    PassengerInformationEquipmentRefStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
