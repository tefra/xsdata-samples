from __future__ import annotations

from dataclasses import dataclass, field

from .fuel_type_enumeration import FuelTypeEnumeration
from .place_equipment_version_structure import PlaceEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RefuellingEquipmentVersionStructure(PlaceEquipmentVersionStructure):
    class Meta:
        name = "RefuellingEquipment_VersionStructure"

    fuel_type: None | FuelTypeEnumeration = field(
        default=None,
        metadata={
            "name": "FuelType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
