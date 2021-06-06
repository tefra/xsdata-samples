from dataclasses import dataclass, field
from typing import List
from .abstract_curve import AbstractCurve
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
            "sequential": True,
        }
    )
    abstract_curve: List[AbstractCurve] = field(
        default_factory=list,
        metadata={
            "name": "AbstractCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequential": True,
        }
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
