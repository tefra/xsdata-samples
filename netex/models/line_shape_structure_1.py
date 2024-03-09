from dataclasses import dataclass, field
from typing import List

from .location_structure_1 import LocationStructure1

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class LineShapeStructure1:
    class Meta:
        name = "LineShapeStructure"

    point: List[LocationStructure1] = field(
        default_factory=list,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 2,
        },
    )
