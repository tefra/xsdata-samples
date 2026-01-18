from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.alert_cpoint import AlertCPoint
from datexii.models.eu.datexii.v2.network_location import NetworkLocation
from datexii.models.eu.datexii.v2.point_along_linear_element import (
    PointAlongLinearElement,
)
from datexii.models.eu.datexii.v2.point_by_coordinates import (
    PointByCoordinates,
)
from datexii.models.eu.datexii.v2.point_extension_type import (
    PointExtensionType,
)
from datexii.models.eu.datexii.v2.tpeg_point_location import TpegPointLocation

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class Point(NetworkLocation):
    """
    A single geospatial point.
    """

    tpeg_point_location: TpegPointLocation | None = field(
        default=None,
        metadata={
            "name": "tpegPointLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    alert_cpoint: AlertCPoint | None = field(
        default=None,
        metadata={
            "name": "alertCPoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    point_along_linear_element: PointAlongLinearElement | None = field(
        default=None,
        metadata={
            "name": "pointAlongLinearElement",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    point_by_coordinates: PointByCoordinates | None = field(
        default=None,
        metadata={
            "name": "pointByCoordinates",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    point_extension: PointExtensionType | None = field(
        default=None,
        metadata={
            "name": "pointExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
