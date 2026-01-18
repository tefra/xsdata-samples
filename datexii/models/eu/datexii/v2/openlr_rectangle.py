from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.point_coordinates import PointCoordinates

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class OpenlrRectangle:
    """
    two geo-coordinate pairs defining the rectangular.

    :ivar openlr_lower_left: The lower left corner of the rectangle
    :ivar openlr_upper_right: the upper right corner of the rectangle
    :ivar openlr_rectangle_extension:
    """

    openlr_lower_left: None | PointCoordinates = field(
        default=None,
        metadata={
            "name": "openlrLowerLeft",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    openlr_upper_right: None | PointCoordinates = field(
        default=None,
        metadata={
            "name": "openlrUpperRight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    openlr_rectangle_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "openlrRectangleExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
