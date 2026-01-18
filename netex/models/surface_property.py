from __future__ import annotations

from dataclasses import dataclass

from .surface_property_type import SurfacePropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(kw_only=True)
class SurfaceProperty(SurfacePropertyType):
    class Meta:
        name = "surfaceProperty"
        namespace = "http://www.opengis.net/gml/3.2"
