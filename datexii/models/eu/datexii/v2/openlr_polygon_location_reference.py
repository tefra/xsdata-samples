from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.openlr_area_location_reference import (
    OpenlrAreaLocationReference,
)
from datexii.models.eu.datexii.v2.openlr_polygon_corners import (
    OpenlrPolygonCorners,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class OpenlrPolygonLocationReference(OpenlrAreaLocationReference):
    """
    the openLR method of areadefinition by providing points that bound the
    area.
    """

    openlr_polygon_corners: OpenlrPolygonCorners | None = field(
        default=None,
        metadata={
            "name": "openlrPolygonCorners",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    openlr_polygon_location_reference_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "openlrPolygonLocationReferenceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
