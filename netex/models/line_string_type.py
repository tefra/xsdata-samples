from dataclasses import dataclass, field
from typing import List, Union
from .abstract_curve_type import AbstractCurveType
from .point_property import PointProperty
from .pos import Pos
from .pos_list import PosList

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class LineStringType(AbstractCurveType):
    pos_or_point_property_or_pos_list: List[
        Union[Pos, PointProperty, PosList]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "pos",
                    "type": Pos,
                    "namespace": "http://www.opengis.net/gml/3.2",
                },
                {
                    "name": "pointProperty",
                    "type": PointProperty,
                    "namespace": "http://www.opengis.net/gml/3.2",
                },
                {
                    "name": "posList",
                    "type": PosList,
                    "namespace": "http://www.opengis.net/gml/3.2",
                },
            ),
        },
    )
