from dataclasses import dataclass
from netex.models.group_of_places_ref_structure import GroupOfPlacesRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupOfPlacesRef(GroupOfPlacesRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
