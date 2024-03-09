from dataclasses import dataclass, field
from typing import List, Optional

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.point_coordinates import PointCoordinates
from datexii.models.eu.datexii.v2.tpeg_other_point_descriptor import (
    TpegOtherPointDescriptor,
)
from datexii.models.eu.datexii.v2.tpeg_point import TpegPoint

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class TpegNonJunctionPoint(TpegPoint):
    """
    A point on the road network which is not a road junction point.

    :ivar point_coordinates:
    :ivar name: A descriptive name which helps to identify the non
        junction point. At least one descriptor must identify the road
        on which the point is located, i.e. must be of type 'linkName'
        or 'localLinkName'.
    :ivar tpeg_non_junction_point_extension:
    """

    point_coordinates: Optional[PointCoordinates] = field(
        default=None,
        metadata={
            "name": "pointCoordinates",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    name: List[TpegOtherPointDescriptor] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        },
    )
    tpeg_non_junction_point_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegNonJunctionPointExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
