from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.point_coordinates import PointCoordinates

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class OpenlrGeoCoordinate:
    """
    A geo-coordinate pair is a position in a map defined by its longitude
    and latitude coordinate values.
    """

    openlr_coordinate: PointCoordinates | None = field(
        default=None,
        metadata={
            "name": "openlrCoordinate",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    openlr_geo_coordinate_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "openlrGeoCoordinateExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
