from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.multilingual_string import MultilingualString
from datexii.models.eu.datexii.v2.polygon_area_index_point_coordinates import (
    PolygonAreaIndexPointCoordinates,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class PolygonArea:
    """
    defines points for a closed polygon-shape describing the area.

    :ivar section_name: Name of the polygon area. Especially useful when
        the area consists of more than one polygon.
    :ivar point_coordinates:
    :ivar polygon_area_extension:
    """

    section_name: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "sectionName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    point_coordinates: list[PolygonAreaIndexPointCoordinates] = field(
        default_factory=list,
        metadata={
            "name": "pointCoordinates",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    polygon_area_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "polygonAreaExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
