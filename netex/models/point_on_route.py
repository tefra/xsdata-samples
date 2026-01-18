from __future__ import annotations

from dataclasses import dataclass

from .point_on_route_versioned_child_structure import (
    PointOnRouteVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointOnRoute(PointOnRouteVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
