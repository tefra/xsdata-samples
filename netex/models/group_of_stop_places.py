from dataclasses import dataclass
from .group_of_stop_places_structure import GroupOfStopPlacesStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupOfStopPlaces(GroupOfStopPlacesStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
