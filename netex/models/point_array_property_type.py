from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .point_1 import Point1

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(kw_only=True)
class PointArrayPropertyType:
    point: Iterable[Point1] = field(
        default_factory=list,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
