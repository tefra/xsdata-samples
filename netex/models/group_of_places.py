from __future__ import annotations

from dataclasses import dataclass

from .group_of_places_version_structure import GroupOfPlacesVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfPlaces(GroupOfPlacesVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
