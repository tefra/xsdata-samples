from dataclasses import dataclass

from .rough_surface_ref_structure import RoughSurfaceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RoughSurfaceRef(RoughSurfaceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
