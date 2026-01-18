from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.point_coordinates import PointCoordinates

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass(kw_only=True)
class PolygonAreaIndexPointCoordinates:
    class Meta:
        name = "_PolygonAreaIndexPointCoordinates"

    point_coordinates: PointCoordinates = field(
        metadata={
            "name": "pointCoordinates",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    index: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
