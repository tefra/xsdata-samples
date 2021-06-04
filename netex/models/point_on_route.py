from dataclasses import dataclass
from netex.models.point_on_route_versioned_child_structure import PointOnRouteVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PointOnRoute(PointOnRouteVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
