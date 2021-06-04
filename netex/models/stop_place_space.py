from dataclasses import dataclass
from netex.models.stop_place_space_version_structure import StopPlaceSpaceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class StopPlaceSpace(StopPlaceSpaceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
