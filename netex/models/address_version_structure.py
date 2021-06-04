from dataclasses import dataclass, field
from typing import Optional
from netex.models.country_ref import CountryRef
from netex.models.multilingual_string import MultilingualString
from netex.models.place_version_structure import PlaceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AddressVersionStructure(PlaceVersionStructure):
    class Meta:
        name = "Address_VersionStructure"

    country_ref: Optional[CountryRef] = field(
        default=None,
        metadata={
            "name": "CountryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    country_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "CountryName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
