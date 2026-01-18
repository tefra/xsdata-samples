from __future__ import annotations

from dataclasses import dataclass, field

from .derived_view_structure import DerivedViewStructure
from .multilingual_string import MultilingualString
from .point_of_interest_ref import PointOfInterestRef
from .type_of_place_refs_rel_structure import TypeOfPlaceRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointOfInterestDerivedViewStructure(DerivedViewStructure):
    class Meta:
        name = "PointOfInterest_DerivedViewStructure"

    point_of_interest_ref: None | PointOfInterestRef = field(
        default=None,
        metadata={
            "name": "PointOfInterestRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    name: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    place_types: None | TypeOfPlaceRefsRelStructure = field(
        default=None,
        metadata={
            "name": "placeTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    short_name: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
