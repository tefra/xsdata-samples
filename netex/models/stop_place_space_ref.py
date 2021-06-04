from dataclasses import dataclass
from netex.models.stop_place_space_ref_structure import StopPlaceSpaceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class StopPlaceSpaceRef(StopPlaceSpaceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
