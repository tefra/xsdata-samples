from dataclasses import dataclass
from .road_junction_version_structure import RoadJunctionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RoadJunction(RoadJunctionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
