from dataclasses import dataclass, field
from typing import List
from .line_string import LineString
from .point_1 import Point1
from .polygon import Polygon

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class GeometryArrayPropertyType:
    polygon: List[Polygon] = field(
        default_factory=list,
        metadata={
            "name": "Polygon",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 34,
        }
    )
    line_string: List[LineString] = field(
        default_factory=list,
        metadata={
            "name": "LineString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 34,
        }
    )
    point: List[Point1] = field(
        default_factory=list,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequence": 34,
        }
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
