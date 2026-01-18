from __future__ import annotations

from dataclasses import dataclass, field

from .country_ref import CountryRef
from .group_of_entities_version_structure import (
    GroupOfEntitiesVersionStructure,
)
from .place_ref_structure import PlaceRefStructure
from .place_refs_rel_structure import PlaceRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfPlacesVersionStructure(GroupOfEntitiesVersionStructure):
    class Meta:
        name = "GroupOfPlaces_VersionStructure"

    members: None | PlaceRefsRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    country_ref: None | CountryRef = field(
        default=None,
        metadata={
            "name": "CountryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    main_place_ref: None | PlaceRefStructure = field(
        default=None,
        metadata={
            "name": "MainPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
