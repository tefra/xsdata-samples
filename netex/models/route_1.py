from dataclasses import dataclass
from netex.models.route_version_structure import RouteVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Route1(RouteVersionStructure):
    class Meta:
        name = "Route"
        namespace = "http://www.netex.org.uk/netex"
