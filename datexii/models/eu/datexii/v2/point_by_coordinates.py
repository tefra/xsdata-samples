from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.point_coordinates import PointCoordinates

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class PointByCoordinates:
    """
    A single point defined only by a coordinate set with an optional
    bearing direction.

    :ivar bearing: A bearing at the point measured in degrees (0 - 359).
        Unless otherwise specified the reference direction corresponding
        to 0 degrees is North.
    :ivar point_coordinates:
    :ivar point_by_coordinates_extension:
    """

    bearing: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    point_coordinates: Optional[PointCoordinates] = field(
        default=None,
        metadata={
            "name": "pointCoordinates",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    point_by_coordinates_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "pointByCoordinatesExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
