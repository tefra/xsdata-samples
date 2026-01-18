from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.predefined_location import PredefinedLocation

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass(kw_only=True)
class PredefinedItineraryIndexPredefinedLocation:
    class Meta:
        name = "_PredefinedItineraryIndexPredefinedLocation"

    predefined_location: PredefinedLocation = field(
        metadata={
            "name": "predefinedLocation",
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
