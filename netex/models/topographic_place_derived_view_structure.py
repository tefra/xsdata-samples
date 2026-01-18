from __future__ import annotations

from dataclasses import dataclass, field

from .country_ref import CountryRef
from .derived_view_structure import DerivedViewStructure
from .multilingual_string import MultilingualString
from .topographic_place_ref import TopographicPlaceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TopographicPlaceDerivedViewStructure(DerivedViewStructure):
    class Meta:
        name = "TopographicPlace_DerivedViewStructure"

    topographic_place_ref: None | TopographicPlaceRef = field(
        default=None,
        metadata={
            "name": "TopographicPlaceRef",
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
    short_name: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    qualifier_name: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "QualifierName",
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
