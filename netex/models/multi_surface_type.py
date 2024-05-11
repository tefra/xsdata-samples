from dataclasses import dataclass, field
from typing import List, Optional

from .abstract_geometric_aggregate_type import AbstractGeometricAggregateType
from .surface_member import SurfaceMember
from .surface_members import SurfaceMembers

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class MultiSurfaceType(AbstractGeometricAggregateType):
    surface_member: List[SurfaceMember] = field(
        default_factory=list,
        metadata={
            "name": "surfaceMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    surface_members: Optional[SurfaceMembers] = field(
        default=None,
        metadata={
            "name": "surfaceMembers",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
