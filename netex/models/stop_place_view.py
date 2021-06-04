from dataclasses import dataclass
from netex.models.stop_place_derived_view_structure import StopPlaceDerivedViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class StopPlaceView(StopPlaceDerivedViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
