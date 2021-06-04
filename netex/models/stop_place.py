from dataclasses import dataclass
from netex.models.stop_place_version_structure import StopPlaceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class StopPlace(StopPlaceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
