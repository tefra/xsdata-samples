from __future__ import annotations

from dataclasses import dataclass, field

from .nil_reason_enumeration_value import NilReasonEnumerationValue
from .point_1 import Point1

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(kw_only=True)
class PointPropertyType:
    point: None | Point1 = field(
        default=None,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    nil_reason: None | str | NilReasonEnumerationValue = field(
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
