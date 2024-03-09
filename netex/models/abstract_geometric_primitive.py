from dataclasses import dataclass

from .abstract_geometric_primitive_type import AbstractGeometricPrimitiveType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractGeometricPrimitive(AbstractGeometricPrimitiveType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
