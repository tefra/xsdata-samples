from dataclasses import dataclass
from netex.models.topographic_place_version_structure import TopographicPlaceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TopographicPlace(TopographicPlaceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
