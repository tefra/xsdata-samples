from dataclasses import dataclass
from netex.models.abstract_geometry_type import AbstractGeometryType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractGeometry(AbstractGeometryType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
