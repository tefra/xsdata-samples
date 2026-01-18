from __future__ import annotations

from dataclasses import dataclass, field

from .country_ref import CountryRef
from .group_of_entities_version_structure import (
    GroupOfEntitiesVersionStructure,
)
from .place_ref_structure import PlaceRefStructure
from .place_refs_rel_structure import PlaceRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupOfPlacesVersionStructure(GroupOfEntitiesVersionStructure):
    class Meta:
        name = "GroupOfPlaces_VersionStructure"

    members: PlaceRefsRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    country_ref: CountryRef | None = field(
        default=None,
        metadata={
            "name": "CountryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    main_place_ref: PlaceRefStructure | None = field(
        default=None,
        metadata={
            "name": "MainPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
