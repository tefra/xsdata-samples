from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class PointCoordinates:
    """
    A pair of coordinates defining the geodetic position of a single point
    using the European Terrestrial Reference System 1989 (ETRS89).

    :ivar latitude: Latitude in decimal degrees using the European
        Terrestrial Reference System 1989 (ETRS89).
    :ivar longitude: Longitude in decimal degrees using the European
        Terrestrial Reference System 1989 (ETRS89).
    :ivar point_coordinates_extension:
    """

    latitude: float | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    longitude: float | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    point_coordinates_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "pointCoordinatesExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
