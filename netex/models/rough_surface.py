from dataclasses import dataclass
from netex.models.rough_surface_structure import RoughSurfaceStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RoughSurface(RoughSurfaceStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
