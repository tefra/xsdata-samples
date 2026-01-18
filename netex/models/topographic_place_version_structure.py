from __future__ import annotations

from dataclasses import dataclass, field

from .accesses_rel_structure import AccessesRelStructure
from .country_ref import CountryRef
from .country_refs_rel_structure import CountryRefsRelStructure
from .place_version_structure import PlaceVersionStructure
from .topographic_place_descriptor_versioned_child_structure import (
    TopographicPlaceDescriptorVersionedChildStructure,
)
from .topographic_place_descriptors_rel_structure import (
    TopographicPlaceDescriptorsRelStructure,
)
from .topographic_place_ref_structure import TopographicPlaceRefStructure
from .topographic_place_refs_rel_structure import (
    TopographicPlaceRefsRelStructure,
)
from .topographic_place_type_enumeration import TopographicPlaceTypeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TopographicPlaceVersionStructure(PlaceVersionStructure):
    class Meta:
        name = "TopographicPlace_VersionStructure"

    iso_code: None | str = field(
        default=None,
        metadata={
            "name": "IsoCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    descriptor: TopographicPlaceDescriptorVersionedChildStructure = field(
        metadata={
            "name": "Descriptor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    alternative_descriptors: None | TopographicPlaceDescriptorsRelStructure = (
        field(
            default=None,
            metadata={
                "name": "alternativeDescriptors",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    topographic_place_type: None | TopographicPlaceTypeEnumeration = field(
        default=None,
        metadata={
            "name": "TopographicPlaceType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    place_centre: None | bool = field(
        default=None,
        metadata={
            "name": "PlaceCentre",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    post_code: None | str = field(
        default=None,
        metadata={
            "name": "PostCode",
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
    other_countries: None | CountryRefsRelStructure = field(
        default=None,
        metadata={
            "name": "otherCountries",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parent_topographic_place_ref: None | TopographicPlaceRefStructure = field(
        default=None,
        metadata={
            "name": "ParentTopographicPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    adjacent_places: None | TopographicPlaceRefsRelStructure = field(
        default=None,
        metadata={
            "name": "adjacentPlaces",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    contained_in: None | TopographicPlaceRefsRelStructure = field(
        default=None,
        metadata={
            "name": "containedIn",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    accesses: None | AccessesRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
