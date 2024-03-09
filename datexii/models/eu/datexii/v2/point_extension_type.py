from dataclasses import dataclass, field
from typing import List, Optional

from datexii.models.eu.datexii.v2.openlr_extended_point import (
    OpenlrExtendedPoint,
)
from datexii.models.eu.datexii.v2.point_extended import PointExtended

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class PointExtensionType:
    class Meta:
        name = "_PointExtensionType"

    openlr_extended_point: Optional[OpenlrExtendedPoint] = field(
        default=None,
        metadata={
            "name": "openlrExtendedPoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    point_extended: Optional[PointExtended] = field(
        default=None,
        metadata={
            "name": "pointExtended",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
