from dataclasses import dataclass
from netex.models.topographic_place_ref_structure import TopographicPlaceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TopographicPlaceRef(TopographicPlaceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
