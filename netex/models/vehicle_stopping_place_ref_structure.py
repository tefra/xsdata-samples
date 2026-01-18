from __future__ import annotations

from dataclasses import dataclass

from .stop_place_space_ref_structure import StopPlaceSpaceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleStoppingPlaceRefStructure(StopPlaceSpaceRefStructure):
    pass
