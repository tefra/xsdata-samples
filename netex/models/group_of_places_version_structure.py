from dataclasses import dataclass, field
from typing import Optional
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

    members: Optional[PlaceRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    country_ref: Optional[CountryRef] = field(
        default=None,
        metadata={
            "name": "CountryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    main_place_ref: Optional[PlaceRefStructure] = field(
        default=None,
        metadata={
            "name": "MainPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
