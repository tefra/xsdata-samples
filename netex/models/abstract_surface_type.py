from dataclasses import dataclass
from .abstract_geometric_primitive_type import AbstractGeometricPrimitiveType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractSurfaceType(AbstractGeometricPrimitiveType):
    pass
