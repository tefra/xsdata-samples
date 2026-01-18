from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.location import Location

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class LocationContainedInItinerary:
    class Meta:
        name = "_LocationContainedInItinerary"

    location: None | Location = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    index: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
