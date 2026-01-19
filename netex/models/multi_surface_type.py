from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .abstract_geometric_aggregate_type import AbstractGeometricAggregateType
from .surface_member import SurfaceMember
from .surface_members import SurfaceMembers

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(kw_only=True)
class MultiSurfaceType(AbstractGeometricAggregateType):
    surface_member: Sequence[SurfaceMember] = field(
        default_factory=list,
        metadata={
            "name": "surfaceMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    surface_members: None | SurfaceMembers = field(
        default=None,
        metadata={
            "name": "surfaceMembers",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
