from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.openlr_base_point_location import (
    OpenlrBasePointLocation,
)
from datexii.models.eu.datexii.v2.point_coordinates import PointCoordinates

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class OpenlrPoiWithAccessPoint(OpenlrBasePointLocation):
    """
    Point along line with access is a point location which is defined by a
    line,an offset value and a coordinate.

    :ivar openlr_coordinate: The coordinate of the actual point of
        interest
    :ivar openlr_poi_with_access_point_extension:
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
    openlr_poi_with_access_point_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "openlrPoiWithAccessPointExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
