from dataclasses import dataclass
from netex.models.place_ref_structure import PlaceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PlaceRef2(PlaceRefStructure):
    class Meta:
        name = "PlaceRef"
        namespace = "http://www.netex.org.uk/netex"
