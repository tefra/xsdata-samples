from dataclasses import dataclass
from .linear_ring_type import LinearRingType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class LinearRing(LinearRingType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
