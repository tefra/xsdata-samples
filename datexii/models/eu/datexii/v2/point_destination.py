from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.destination import Destination
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.point import Point

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class PointDestination(Destination):
    """
    The specification of the destination of a defined route or itinerary
    which is a point.
    """

    point: None | Point = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    point_destination_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "pointDestinationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
