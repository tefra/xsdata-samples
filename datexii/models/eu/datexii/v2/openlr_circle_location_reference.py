from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.openlr_area_location_reference import (
    OpenlrAreaLocationReference,
)
from datexii.models.eu.datexii.v2.openlr_geo_coordinate import (
    OpenlrGeoCoordinate,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class OpenlrCircleLocationReference(OpenlrAreaLocationReference):
    """
    The openLR method of areadefinition by providing a center position and a
    radius.

    :ivar radius: The radius of the geometric area identified.
    :ivar openlr_geo_coordinate:
    :ivar openlr_circle_location_reference_extension:
    """

    radius: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    openlr_geo_coordinate: Optional[OpenlrGeoCoordinate] = field(
        default=None,
        metadata={
            "name": "openlrGeoCoordinate",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    openlr_circle_location_reference_extension: Optional[ExtensionType] = (
        field(
            default=None,
            metadata={
                "name": "openlrCircleLocationReferenceExtension",
                "type": "Element",
                "namespace": "http://datex2.eu/schema/2/2_0",
            },
        )
    )
