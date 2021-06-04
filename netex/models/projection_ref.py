from dataclasses import dataclass
from netex.models.projection_ref_structure import ProjectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ProjectionRef(ProjectionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
