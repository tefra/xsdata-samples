from dataclasses import dataclass, field
from typing import List
from .line_string import LineString

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class CurveArrayPropertyType:
    line_string: List[LineString] = field(
        default_factory=list,
        metadata={
            "name": "LineString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
