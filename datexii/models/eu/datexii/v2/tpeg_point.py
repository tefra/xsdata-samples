from dataclasses import dataclass, field
from typing import Optional
from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class TpegPoint:
    """
    A point on the road network which is either a junction point or a non
    junction point.
    """
    tpeg_point_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegPointExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
