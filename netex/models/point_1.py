from dataclasses import dataclass
from .point_type import PointType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class Point1(PointType):
    class Meta:
        name = "Point"
        namespace = "http://www.opengis.net/gml/3.2"
