from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.tpeg_loc04_height_type_enum import (
    TpegLoc04HeightTypeEnum,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class TpegHeight:
    """
    Height information which provides additional discrimination for the
    applicable area.

    :ivar height: A measurement of height in metres
    :ivar height_type: A descriptive identification of relative height
        using TPEG-Loc location referencing.
    :ivar tpeg_height_extension:
    """

    height: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    height_type: Optional[TpegLoc04HeightTypeEnum] = field(
        default=None,
        metadata={
            "name": "heightType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    tpeg_height_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegHeightExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
