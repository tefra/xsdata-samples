from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.direction_enum import DirectionEnum
from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class TpegPointLocation:
    """
    A single point on the road network defined by a TPEG-Loc structure and
    which has an associated direction of traffic flow.

    :ivar tpeg_direction: The direction of traffic flow.
    :ivar tpeg_point_location_extension:
    """

    tpeg_direction: Optional[DirectionEnum] = field(
        default=None,
        metadata={
            "name": "tpegDirection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    tpeg_point_location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegPointLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
