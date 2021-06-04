from dataclasses import dataclass
from netex.models.infrastructure_point_version_structure import InfrastructurePointVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RailwayJunctionVersionStructure(InfrastructurePointVersionStructure):
    class Meta:
        name = "RailwayJunction_VersionStructure"
