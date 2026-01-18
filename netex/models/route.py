from __future__ import annotations

from dataclasses import dataclass

from .route_version_structure import RouteVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Route(RouteVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
