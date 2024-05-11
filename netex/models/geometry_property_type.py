from dataclasses import dataclass, field
from typing import Optional, Union

from .line_string import LineString
from .multi_surface import MultiSurface
from .nil_reason_enumeration_value import NilReasonEnumerationValue
from .point_1 import Point1
from .polygon import Polygon

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class GeometryPropertyType:
    choice: Optional[Union[MultiSurface, Polygon, LineString, Point1]] = field(
        default=None,
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
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:\w{2,}",
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
