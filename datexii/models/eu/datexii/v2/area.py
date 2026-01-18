from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.alert_carea import AlertCArea
from datexii.models.eu.datexii.v2.area_extension_type import AreaExtensionType
from datexii.models.eu.datexii.v2.location import Location
from datexii.models.eu.datexii.v2.tpeg_area_location import TpegAreaLocation

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class Area(Location):
    """
    A geographic or geometric defined area which may be qualified by height
    information to provide additional geospatial discrimination (e.g. for
    snow in an area but only above a certain altitude).
    """

    alert_carea: AlertCArea | None = field(
        default=None,
        metadata={
            "name": "alertCArea",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    tpeg_area_location: TpegAreaLocation | None = field(
        default=None,
        metadata={
            "name": "tpegAreaLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    area_extension: AreaExtensionType | None = field(
        default=None,
        metadata={
            "name": "areaExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
