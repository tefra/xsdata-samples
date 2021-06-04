from dataclasses import dataclass, field
from typing import List
from netex.models.abstract_curve import AbstractCurve
from netex.models.abstract_geometric_primitive import AbstractGeometricPrimitive
from netex.models.abstract_geometry import AbstractGeometry
from netex.models.abstract_surface import AbstractSurface
from netex.models.line_string import LineString
from netex.models.point_1 import Point1
from netex.models.polygon import Polygon

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class GeometryArrayPropertyType:
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
    point: List[Point1] = field(
        default_factory=list,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequential": True,
        }
    )
    abstract_geometric_primitive: List[AbstractGeometricPrimitive] = field(
        default_factory=list,
        metadata={
            "name": "AbstractGeometricPrimitive",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "sequential": True,
        }
    )
    abstract_geometry: List[AbstractGeometry] = field(
        default_factory=list,
        metadata={
            "name": "AbstractGeometry",
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
