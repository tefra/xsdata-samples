from __future__ import annotations

from dataclasses import dataclass

from .route_derived_view_structure import RouteDerivedViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RouteView(RouteDerivedViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
