from dataclasses import dataclass, field
from typing import List
from .abstract_surface import AbstractSurface
from .polygon import Polygon

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class SurfaceArrayPropertyType:
    polygon: List[Polygon] = field(
        default_factory=list,
        metadata={
            "name": "Polygon",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequential": True,
        }
    )
    abstract_surface: List[AbstractSurface] = field(
        default_factory=list,
        metadata={
            "name": "AbstractSurface",
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
