from dataclasses import dataclass, field
from typing import Optional

from .place_version_structure import PlaceVersionStructure
from .postal_address import PostalAddress
from .road_address import RoadAddress

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AddressablePlaceVersionStructure(PlaceVersionStructure):
    class Meta:
        name = "AddressablePlace_VersionStructure"

    url: Optional[str] = field(
        default=None,
        metadata={
            "name": "Url",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    image: Optional[str] = field(
        default=None,
        metadata={
            "name": "Image",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    postal_address: Optional[PostalAddress] = field(
        default=None,
        metadata={
            "name": "PostalAddress",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    road_address: Optional[RoadAddress] = field(
        default=None,
        metadata={
            "name": "RoadAddress",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
