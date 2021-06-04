from dataclasses import dataclass
from netex.models.route_point_version_structure import RoutePointVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RoutePoint(RoutePointVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
