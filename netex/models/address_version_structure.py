from __future__ import annotations

from dataclasses import dataclass, field

from .country_ref import CountryRef
from .multilingual_string import MultilingualString
from .place_version_structure import PlaceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AddressVersionStructure(PlaceVersionStructure):
    class Meta:
        name = "Address_VersionStructure"

    country_ref: None | CountryRef = field(
        default=None,
        metadata={
            "name": "CountryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    country_name: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "CountryName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
