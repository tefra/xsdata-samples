from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.openlr_geo_coordinate import (
    OpenlrGeoCoordinate,
)
from datexii.models.eu.datexii.v2.openlr_poi_with_access_point import (
    OpenlrPoiWithAccessPoint,
)
from datexii.models.eu.datexii.v2.openlr_point_along_line import (
    OpenlrPointAlongLine,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class OpenlrPointLocationReference:
    """
    A point location is a zero-dimensional element in a map that specifies
    a geometric location.
    """

    openlr_geo_coordinate: None | OpenlrGeoCoordinate = field(
        default=None,
        metadata={
            "name": "openlrGeoCoordinate",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    openlr_poi_with_access_point: None | OpenlrPoiWithAccessPoint = field(
        default=None,
        metadata={
            "name": "openlrPoiWithAccessPoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    openlr_point_along_line: None | OpenlrPointAlongLine = field(
        default=None,
        metadata={
            "name": "openlrPointAlongLine",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    openlr_point_location_reference_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "openlrPointLocationReferenceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
