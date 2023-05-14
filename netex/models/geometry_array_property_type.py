from dataclasses import dataclass, field
from typing import List
from .line_string import LineString
from .point_1 import Point1
from .polygon import Polygon

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class GeometryArrayPropertyType:
    polygon_or_line_string_or_point: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Polygon",
                    "type": Polygon,
                    "namespace": "http://www.opengis.net/gml/3.2",
                },
                {
                    "name": "LineString",
                    "type": LineString,
                    "namespace": "http://www.opengis.net/gml/3.2",
                },
                {
                    "name": "Point",
                    "type": Point1,
                    "namespace": "http://www.opengis.net/gml/3.2",
                },
            ),
        }
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
