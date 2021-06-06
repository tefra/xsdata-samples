from dataclasses import dataclass
from .vector_type import VectorType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class Vector(VectorType):
    class Meta:
        name = "vector"
        namespace = "http://www.opengis.net/gml/3.2"
