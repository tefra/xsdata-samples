from dataclasses import dataclass
from netex.models.polygon_type import PolygonType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class Polygon(PolygonType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
