from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.openlr_last_location_reference_point import (
    OpenlrLastLocationReferencePoint,
)
from datexii.models.eu.datexii.v2.openlr_location_reference_point import (
    OpenlrLocationReferencePoint,
)
from datexii.models.eu.datexii.v2.openlr_orientation_enum import (
    OpenlrOrientationEnum,
)
from datexii.models.eu.datexii.v2.openlr_side_of_road_enum import (
    OpenlrSideOfRoadEnum,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class OpenlrBasePointLocation:
    """
    Holds common data that are used both in OpenlrPointAccessPoint and
    OpenlrPointAlongLine.

    :ivar openlr_side_of_road: Side of road
    :ivar openlr_orientation: Orientation
    :ivar openlr_positive_offset: The positive offset along the line of
        the location.
    :ivar openlr_location_reference_point:
    :ivar openlr_last_location_reference_point:
    :ivar openlr_base_point_location_extension:
    """

    openlr_side_of_road: Optional[OpenlrSideOfRoadEnum] = field(
        default=None,
        metadata={
            "name": "openlrSideOfRoad",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    openlr_orientation: Optional[OpenlrOrientationEnum] = field(
        default=None,
        metadata={
            "name": "openlrOrientation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    openlr_positive_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "openlrPositiveOffset",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    openlr_location_reference_point: Optional[OpenlrLocationReferencePoint] = (
        field(
            default=None,
            metadata={
                "name": "openlrLocationReferencePoint",
                "type": "Element",
                "namespace": "http://datex2.eu/schema/2/2_0",
                "required": True,
            },
        )
    )
    openlr_last_location_reference_point: Optional[
        OpenlrLastLocationReferencePoint
    ] = field(
        default=None,
        metadata={
            "name": "openlrLastLocationReferencePoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    openlr_base_point_location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "openlrBasePointLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
