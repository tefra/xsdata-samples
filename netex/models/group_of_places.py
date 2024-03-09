from dataclasses import dataclass

from .group_of_places_version_structure import GroupOfPlacesVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupOfPlaces(GroupOfPlacesVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
