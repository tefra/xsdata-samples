from dataclasses import dataclass, field
from typing import List, Optional
from npo.models.geo_location_type import GeoLocationType
from npo.models.owner_type_enum import OwnerTypeEnum

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class GeoLocationsType:
    class Meta:
        name = "geoLocationsType"

    geo_location: List[GeoLocationType] = field(
        default_factory=list,
        metadata={
            "name": "geoLocation",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    owner: Optional[OwnerTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
