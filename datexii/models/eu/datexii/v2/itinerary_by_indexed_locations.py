from dataclasses import dataclass, field
from typing import List, Optional

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.itinerary import Itinerary
from datexii.models.eu.datexii.v2.location_contained_in_itinerary import (
    LocationContainedInItinerary,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class ItineraryByIndexedLocations(Itinerary):
    """Multiple physically separate locations arranged as an ordered set that
    defines an itinerary or route.

    The index qualifier indicates the order.

    :ivar location_contained_in_itinerary: A location contained in an
        itinerary (i.e. an ordered set of locations defining a route or
        itinerary).
    :ivar itinerary_by_indexed_locations_extension:
    """

    location_contained_in_itinerary: List[LocationContainedInItinerary] = (
        field(
            default_factory=list,
            metadata={
                "name": "locationContainedInItinerary",
                "type": "Element",
                "namespace": "http://datex2.eu/schema/2/2_0",
            },
        )
    )
    itinerary_by_indexed_locations_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "itineraryByIndexedLocationsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
