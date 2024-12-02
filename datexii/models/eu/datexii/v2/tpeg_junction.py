from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.point_coordinates import PointCoordinates
from datexii.models.eu.datexii.v2.tpeg_ilc_point_descriptor import (
    TpegIlcPointDescriptor,
)
from datexii.models.eu.datexii.v2.tpeg_junction_point_descriptor import (
    TpegJunctionPointDescriptor,
)
from datexii.models.eu.datexii.v2.tpeg_other_point_descriptor import (
    TpegOtherPointDescriptor,
)
from datexii.models.eu.datexii.v2.tpeg_point import TpegPoint

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class TpegJunction(TpegPoint):
    """
    A point on the road network which is a road junction point.

    :ivar point_coordinates:
    :ivar name: A name which identifies a junction point on the road
        network
    :ivar ilc: A descriptor for describing a junction by identifying the
        intersecting roads at a road junction.
    :ivar other_name: A descriptive name which helps to identify the
        junction point.
    :ivar tpeg_junction_extension:
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
    name: Optional[TpegJunctionPointDescriptor] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    ilc: list[TpegIlcPointDescriptor] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
            "max_occurs": 3,
        },
    )
    other_name: list[TpegOtherPointDescriptor] = field(
        default_factory=list,
        metadata={
            "name": "otherName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    tpeg_junction_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegJunctionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
