from dataclasses import dataclass, field
from typing import Optional, Union
from netex.models.nil_reason_enumeration_value import NilReasonEnumerationValue
from netex.models.point_1 import Point1

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class PointPropertyType:
    point: Optional[Point1] = field(
        default=None,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
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
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
