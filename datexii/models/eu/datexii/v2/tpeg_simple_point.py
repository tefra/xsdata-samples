from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.tpeg_loc01_simple_point_location_subtype_enum import (
    TpegLoc01SimplePointLocationSubtypeEnum,
)
from datexii.models.eu.datexii.v2.tpeg_point import TpegPoint
from datexii.models.eu.datexii.v2.tpeg_point_location import TpegPointLocation

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class TpegSimplePoint(TpegPointLocation):
    """
    A point on the road network which is not bounded by any other points on
    the road network.

    :ivar tpeg_simple_point_location_type: The type of TPEG location.
    :ivar point: A single point defined by a coordinate set and TPEG
        decriptors.
    :ivar tpeg_simple_point_extension:
    """

    tpeg_simple_point_location_type: (
        None | TpegLoc01SimplePointLocationSubtypeEnum
    ) = field(
        default=None,
        metadata={
            "name": "tpegSimplePointLocationType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    point: None | TpegPoint = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    tpeg_simple_point_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "tpegSimplePointExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
