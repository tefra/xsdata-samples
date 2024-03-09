from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.itinerary import Itinerary
from datexii.models.eu.datexii.v2.predefined_itinerary_versioned_reference import (
    PredefinedItineraryVersionedReference,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class ItineraryByReference(Itinerary):
    """
    Multiple (i.e. more than one) physically separate locations which are ordered
    that constitute an itinerary or route where they are defined by reference to a
    predefined itinerary.

    :ivar predefined_itinerary_reference: A reference to a versioned
        instance of a predefined itinerary as specified in a
        PredefinedLocationsPublication.
    :ivar itinerary_by_reference_extension:
    """

    predefined_itinerary_reference: Optional[
        PredefinedItineraryVersionedReference
    ] = field(
        default=None,
        metadata={
            "name": "predefinedItineraryReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    itinerary_by_reference_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "itineraryByReferenceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
