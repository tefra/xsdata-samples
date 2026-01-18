from __future__ import annotations

from dataclasses import dataclass

from .place_equipment_ref_structure import PlaceEquipmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class HeadingSignRefStructure(PlaceEquipmentRefStructure):
    pass
