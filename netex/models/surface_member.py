from __future__ import annotations

from dataclasses import dataclass

from .surface_property_type import SurfacePropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class SurfaceMember(SurfacePropertyType):
    class Meta:
        name = "surfaceMember"
        namespace = "http://www.opengis.net/gml/3.2"
