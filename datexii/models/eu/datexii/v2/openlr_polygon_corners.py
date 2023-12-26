from dataclasses import dataclass, field
from typing import List, Optional
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.point_coordinates import PointCoordinates

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class OpenlrPolygonCorners:
    """Geo-coordinate pairs.

    The coordinate pairs defining the corners of the underlying
    geometrical polygon.
    """

    openlr_coordinate: List[PointCoordinates] = field(
        default_factory=list,
        metadata={
            "name": "openlrCoordinate",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 3,
        },
    )
    openlr_polygon_corners_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "openlrPolygonCornersExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
