from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.openlr_base_point_location import (
    OpenlrBasePointLocation,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class OpenlrPointAlongLine(OpenlrBasePointLocation):
    """
    Point along a line.
    """

    openlr_point_along_line_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "openlrPointAlongLineExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
