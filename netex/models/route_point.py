from __future__ import annotations

from dataclasses import dataclass

from .route_point_version_structure import RoutePointVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RoutePoint(RoutePointVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
