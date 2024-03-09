from dataclasses import dataclass

from .topographic_place_derived_view_structure import (
    TopographicPlaceDerivedViewStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TopographicPlaceView(TopographicPlaceDerivedViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
