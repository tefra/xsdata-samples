from dataclasses import dataclass
from .stop_place_version_structure import StopPlaceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class StopPlace1(StopPlaceVersionStructure):
    class Meta:
        name = "StopPlace"
        namespace = "http://www.netex.org.uk/netex"
