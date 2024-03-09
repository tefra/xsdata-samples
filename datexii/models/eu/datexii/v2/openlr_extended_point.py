from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.openlr_point_location_reference import (
    OpenlrPointLocationReference,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class OpenlrExtendedPoint:
    """
    Extension class for OpenLR point.
    """

    openlr_point_location_reference: Optional[OpenlrPointLocationReference] = (
        field(
            default=None,
            metadata={
                "name": "openlrPointLocationReference",
                "type": "Element",
                "namespace": "http://datex2.eu/schema/2/2_0",
                "required": True,
            },
        )
    )
