from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.multilingual_string import MultilingualString
from datexii.models.eu.datexii.v2.predefined_itinerary_index_predefined_location import (
    PredefinedItineraryIndexPredefinedLocation,
)
from datexii.models.eu.datexii.v2.predefined_location_container import (
    PredefinedLocationContainer,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class PredefinedItinerary(PredefinedLocationContainer):
    """
    An identifiable versioned instance of a predefined itinerary.

    :ivar predefined_itinerary_name: A name assigned to the predefined
        itinerary.
    :ivar predefined_location:
    :ivar predefined_itinerary_extension:
    :ivar id:
    :ivar version:
    """

    predefined_itinerary_name: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "predefinedItineraryName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    predefined_location: list[PredefinedItineraryIndexPredefinedLocation] = (
        field(
            default_factory=list,
            metadata={
                "name": "predefinedLocation",
                "type": "Element",
                "namespace": "http://datex2.eu/schema/2/2_0",
            },
        )
    )
    predefined_itinerary_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "predefinedItineraryExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
