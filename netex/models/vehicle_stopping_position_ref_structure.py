from dataclasses import dataclass

from .stop_place_space_ref_structure import StopPlaceSpaceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleStoppingPositionRefStructure(StopPlaceSpaceRefStructure):
    pass
