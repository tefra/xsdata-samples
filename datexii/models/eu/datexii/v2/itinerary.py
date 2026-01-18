from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.destination import Destination
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.group_of_locations import GroupOfLocations

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class Itinerary(GroupOfLocations):
    """
    Multiple (i.e. more than one) physically separate locations arranged as
    an ordered set that defines an itinerary or route.

    :ivar route_destination: Destination of a route or final location in
        an itinerary.
    :ivar itinerary_extension:
    """

    route_destination: list[Destination] = field(
        default_factory=list,
        metadata={
            "name": "routeDestination",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    itinerary_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "itineraryExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
