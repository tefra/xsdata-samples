from dataclasses import dataclass, field
from typing import Optional
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.tpeg_height import TpegHeight
from datexii.models.eu.datexii.v2.tpeg_loc01_area_location_subtype_enum import (
    TpegLoc01AreaLocationSubtypeEnum,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class TpegAreaLocation:
    """
    A geographic or geometric area defined by a TPEG-Loc structure which may
    include height information for additional geospatial discrimination.

    :ivar tpeg_area_location_type: The type of TPEG location.
    :ivar tpeg_height:
    :ivar tpeg_area_location_extension:
    """

    tpeg_area_location_type: Optional[
        TpegLoc01AreaLocationSubtypeEnum
    ] = field(
        default=None,
        metadata={
            "name": "tpegAreaLocationType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    tpeg_height: Optional[TpegHeight] = field(
        default=None,
        metadata={
            "name": "tpegHeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    tpeg_area_location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegAreaLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
