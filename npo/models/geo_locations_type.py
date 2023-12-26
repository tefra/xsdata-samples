from __future__ import annotations
from dataclasses import dataclass, field
from npo.models.geo_location_type import GeoLocationType
from npo.models.owner_type_enum import OwnerTypeEnum

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class GeoLocationsType:
    class Meta:
        name = "geoLocationsType"

    geo_location: list[GeoLocationType] = field(
        default_factory=list,
        metadata={
            "name": "geoLocation",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        },
    )
    owner: None | OwnerTypeEnum = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
