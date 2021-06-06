from dataclasses import dataclass
from .route_derived_view_structure import RouteDerivedViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RouteView(RouteDerivedViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
