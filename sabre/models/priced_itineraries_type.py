from __future__ import annotations

from dataclasses import dataclass, field

from sabre.models.priced_itinerary_type import PricedItineraryType

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class PricedItinerariesType:
    """
    Container for priced itineraries.

    Attributes:
        priced_itinerary: Container for priced itinerary type.
    """

    priced_itinerary: list[PricedItineraryType] = field(
        default_factory=list,
        metadata={
            "name": "PricedItinerary",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "min_occurs": 1,
        },
    )
