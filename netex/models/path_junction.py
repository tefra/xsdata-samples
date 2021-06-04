from dataclasses import dataclass
from netex.models.path_junction_version_structure import PathJunctionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PathJunction(PathJunctionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
