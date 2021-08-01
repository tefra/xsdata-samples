from dataclasses import dataclass, field
from typing import List
from npo.models.location_type import LocationType

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class LocationsType:
    class Meta:
        name = "locationsType"

    location: List[LocationType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
