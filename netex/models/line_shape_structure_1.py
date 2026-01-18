from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .location_structure_1 import LocationStructure1

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class LineShapeStructure1:
    class Meta:
        name = "LineShapeStructure"

    point: Iterable[LocationStructure1] = field(
        default_factory=list,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 2,
        },
    )
