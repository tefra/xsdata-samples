from dataclasses import dataclass
from .route_ref_structure import RouteRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RouteRef(RouteRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
