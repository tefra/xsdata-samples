from dataclasses import dataclass, field
from typing import List, Union

from .line_string import LineString
from .multi_surface import MultiSurface
from .point_1 import Point1
from .polygon import Polygon

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class GeometryArrayPropertyType:
    choice: List[Union[MultiSurface, Polygon, LineString, Point1]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "MultiSurface",
                    "type": MultiSurface,
                    "namespace": "http://www.opengis.net/gml/3.2",
                },
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
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
