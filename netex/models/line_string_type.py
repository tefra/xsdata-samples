from dataclasses import dataclass, field
from typing import List, Optional
from .abstract_curve_type import AbstractCurveType
from .point_property import PointProperty
from .pos import Pos
from .pos_list import PosList

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class LineStringType(AbstractCurveType):
    pos: List[Pos] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "min_occurs": 2,
            "sequential": True,
        }
    )
    point_property: List[PointProperty] = field(
        default_factory=list,
        metadata={
            "name": "pointProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "min_occurs": 2,
            "sequential": True,
        }
    )
    pos_list: Optional[PosList] = field(
        default=None,
        metadata={
            "name": "posList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )