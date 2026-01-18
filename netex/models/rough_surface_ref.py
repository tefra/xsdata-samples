from __future__ import annotations

from dataclasses import dataclass

from .rough_surface_ref_structure import RoughSurfaceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RoughSurfaceRef(RoughSurfaceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
