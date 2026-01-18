from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.openlr_area_location_reference import (
    OpenlrAreaLocationReference,
)
from datexii.models.eu.datexii.v2.openlr_geo_coordinate import (
    OpenlrGeoCoordinate,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass(kw_only=True)
class OpenlrCircleLocationReference(OpenlrAreaLocationReference):
    """
    the openLR method of areadefinition by providing a center position and
    a radius.

    :ivar radius: The radius of the geometric area identified.
    :ivar openlr_geo_coordinate:
    :ivar openlr_circle_location_reference_extension:
    """

    radius: int = field(
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    openlr_geo_coordinate: OpenlrGeoCoordinate = field(
        metadata={
            "name": "openlrGeoCoordinate",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    openlr_circle_location_reference_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "openlrCircleLocationReferenceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
