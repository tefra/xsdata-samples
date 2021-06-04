from dataclasses import dataclass
from netex.models.topographic_projection_version_structure import TopographicProjectionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TopographicProjection(TopographicProjectionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
