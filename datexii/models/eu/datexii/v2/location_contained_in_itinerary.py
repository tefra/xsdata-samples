from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.location import Location

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass(kw_only=True)
class LocationContainedInItinerary:
    class Meta:
        name = "_LocationContainedInItinerary"

    location: Location = field(
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    index: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
