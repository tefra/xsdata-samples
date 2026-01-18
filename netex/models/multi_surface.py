from __future__ import annotations

from dataclasses import dataclass

from .multi_surface_type import MultiSurfaceType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class MultiSurface(MultiSurfaceType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
