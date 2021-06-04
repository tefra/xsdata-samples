from dataclasses import dataclass
from netex.models.route_link_version_structure import RouteLinkVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RouteLink(RouteLinkVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
