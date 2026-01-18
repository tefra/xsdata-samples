from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.rgbcolour import RGBColour

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass(kw_only=True)
class ParkingRoute:
    """
    A parking route, defined by ParkingRouteDetails or by a reference.

    :ivar parking_route_colour: A colour assigned to a parking route for
        visualisation purpose.
    :ivar parking_route_extension:
    """

    parking_route_colour: None | RGBColour = field(
        default=None,
        metadata={
            "name": "parkingRouteColour",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_route_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "parkingRouteExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
