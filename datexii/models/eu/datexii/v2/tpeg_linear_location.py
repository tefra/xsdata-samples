from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.direction_enum import DirectionEnum
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.tpeg_loc01_linear_location_subtype_enum import (
    TpegLoc01LinearLocationSubtypeEnum,
)
from datexii.models.eu.datexii.v2.tpeg_point import TpegPoint

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass(kw_only=True)
class TpegLinearLocation:
    """
    A linear section along a single road defined between two points on the
    same road by a TPEG-Loc structure.

    :ivar tpeg_direction: The direction of traffic flow.
    :ivar tpeg_linear_location_type: The type of TPEG location.
    :ivar to: The location at the down stream end of the linear section
        of road.
    :ivar from_value: The location at the up stream end of the linear
        section of road.
    :ivar tpeg_linear_location_extension:
    """

    tpeg_direction: DirectionEnum = field(
        metadata={
            "name": "tpegDirection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    tpeg_linear_location_type: TpegLoc01LinearLocationSubtypeEnum = field(
        metadata={
            "name": "tpegLinearLocationType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    to: TpegPoint = field(
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    from_value: TpegPoint = field(
        metadata={
            "name": "from",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    tpeg_linear_location_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "tpegLinearLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
