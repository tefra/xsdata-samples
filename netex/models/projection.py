from dataclasses import dataclass
from netex.models.projection_version_structure import ProjectionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Projection(ProjectionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
