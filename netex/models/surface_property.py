from dataclasses import dataclass
from netex.models.surface_property_type import SurfacePropertyType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class SurfaceProperty(SurfacePropertyType):
    class Meta:
        name = "surfaceProperty"
        namespace = "http://www.opengis.net/gml/3.2"
