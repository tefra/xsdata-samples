from __future__ import annotations

from dataclasses import dataclass, field

from .place_version_structure import PlaceVersionStructure
from .postal_address import PostalAddress
from .road_address import RoadAddress

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AddressablePlaceVersionStructure(PlaceVersionStructure):
    class Meta:
        name = "AddressablePlace_VersionStructure"

    url: None | str = field(
        default=None,
        metadata={
            "name": "Url",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    image: None | str = field(
        default=None,
        metadata={
            "name": "Image",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    postal_address: None | PostalAddress = field(
        default=None,
        metadata={
            "name": "PostalAddress",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    road_address: None | RoadAddress = field(
        default=None,
        metadata={
            "name": "RoadAddress",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
