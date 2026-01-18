from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.point_coordinates import PointCoordinates
from datexii.models.eu.datexii.v2.tpeg_area_descriptor import (
    TpegAreaDescriptor,
)
from datexii.models.eu.datexii.v2.tpeg_area_location import TpegAreaLocation

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass(kw_only=True)
class TpegGeometricArea(TpegAreaLocation):
    """
    A geometric area defined by a centre point and a radius.

    :ivar radius: The radius of the geometric area identified.
    :ivar centre_point: Centre point of a circular geometric area.
    :ivar name: Name of area.
    :ivar tpeg_geometric_area_extension:
    """

    radius: int = field(
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    centre_point: PointCoordinates = field(
        metadata={
            "name": "centrePoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    name: None | TpegAreaDescriptor = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    tpeg_geometric_area_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "tpegGeometricAreaExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
