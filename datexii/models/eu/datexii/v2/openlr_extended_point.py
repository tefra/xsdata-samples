from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.openlr_point_location_reference import (
    OpenlrPointLocationReference,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass(kw_only=True)
class OpenlrExtendedPoint:
    """
    Extension class for OpenLR point.
    """

    openlr_point_location_reference: OpenlrPointLocationReference = field(
        metadata={
            "name": "openlrPointLocationReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
