from dataclasses import dataclass, field
from typing import Optional
from .abstract_geometric_primitive_type import AbstractGeometricPrimitiveType
from .pos import Pos

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class PointType(AbstractGeometricPrimitiveType):
    pos: Optional[Pos] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
