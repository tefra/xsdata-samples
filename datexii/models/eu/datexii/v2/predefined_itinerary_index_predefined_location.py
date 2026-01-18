from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.predefined_location import PredefinedLocation

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class PredefinedItineraryIndexPredefinedLocation:
    class Meta:
        name = "_PredefinedItineraryIndexPredefinedLocation"

    predefined_location: PredefinedLocation | None = field(
        default=None,
        metadata={
            "name": "predefinedLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    index: int | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
