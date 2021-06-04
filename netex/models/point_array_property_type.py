from dataclasses import dataclass, field
from typing import List
from netex.models.point_1 import Point1

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class PointArrayPropertyType:
    point: List[Point1] = field(
        default_factory=list,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
