from __future__ import annotations

from dataclasses import dataclass

from .rough_surface_structure import RoughSurfaceStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RoughSurface(RoughSurfaceStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
