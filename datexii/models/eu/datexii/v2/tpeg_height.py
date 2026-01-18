from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.tpeg_loc04_height_type_enum import (
    TpegLoc04HeightTypeEnum,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass(kw_only=True)
class TpegHeight:
    """
    Height information which provides additional discrimination for the
    applicable area.

    :ivar height: A measurement of height in metres
    :ivar height_type: A descriptive identification of relative height
        using TPEG-Loc location referencing.
    :ivar tpeg_height_extension:
    """

    height: None | float = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    height_type: TpegLoc04HeightTypeEnum = field(
        metadata={
            "name": "heightType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    tpeg_height_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "tpegHeightExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
