from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.tpeg_loc01_framed_point_location_subtype_enum import (
    TpegLoc01FramedPointLocationSubtypeEnum,
)
from datexii.models.eu.datexii.v2.tpeg_non_junction_point import (
    TpegNonJunctionPoint,
)
from datexii.models.eu.datexii.v2.tpeg_point import TpegPoint
from datexii.models.eu.datexii.v2.tpeg_point_location import TpegPointLocation

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class TpegFramedPoint(TpegPointLocation):
    """
    A point on the road network which is framed between two other points on
    the same road.

    :ivar tpeg_framed_point_location_type: The type of TPEG location.
    :ivar framed_point: A single non junction point on the road network
        which is framed between two other specified points on the road
        network.
    :ivar to: The location at the down stream end of the section of road
        which frames the TPEGFramedPoint.
    :ivar from_value: The location at the up stream end of the section
        of road which frames the TPEGFramedPoint.
    :ivar tpeg_framed_point_extension:
    """

    tpeg_framed_point_location_type: (
        TpegLoc01FramedPointLocationSubtypeEnum | None
    ) = field(
        default=None,
        metadata={
            "name": "tpegFramedPointLocationType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    framed_point: TpegNonJunctionPoint | None = field(
        default=None,
        metadata={
            "name": "framedPoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    to: TpegPoint | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    from_value: TpegPoint | None = field(
        default=None,
        metadata={
            "name": "from",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    tpeg_framed_point_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "tpegFramedPointExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
