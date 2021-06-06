from dataclasses import dataclass, field
from typing import Optional, Union
from .abstract_curve import AbstractCurve
from .abstract_geometric_primitive import AbstractGeometricPrimitive
from .abstract_surface import AbstractSurface
from .line_string import LineString
from .nil_reason_enumeration_value import NilReasonEnumerationValue
from .point_1 import Point1
from .polygon import Polygon

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class GeometricPrimitivePropertyType:
    polygon: Optional[Polygon] = field(
        default=None,
        metadata={
            "name": "Polygon",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    abstract_surface: Optional[AbstractSurface] = field(
        default=None,
        metadata={
            "name": "AbstractSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    line_string: Optional[LineString] = field(
        default=None,
        metadata={
            "name": "LineString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    abstract_curve: Optional[AbstractCurve] = field(
        default=None,
        metadata={
            "name": "AbstractCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    point: Optional[Point1] = field(
        default=None,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        }
    )
    abstract_geometric_primitive: Optional[AbstractGeometricPrimitive] = field(
        default=None,
        metadata={
            "name": "AbstractGeometricPrimitive",
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
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:\w{2,}",
        }
    )
