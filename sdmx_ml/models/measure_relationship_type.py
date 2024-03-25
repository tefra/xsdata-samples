from dataclasses import dataclass, field
from typing import Tuple

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class MeasureRelationshipType:
    """
    MeasureRelationshipType allows for the description of an attributes
    relationship to one or more measures.

    :ivar measure: This is a reference to a measure defined in this data
        structure definition.
    """

    measure: Tuple[str, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Measure",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "min_occurs": 1,
            "pattern": r"[A-Za-z][A-Za-z0-9_\-]*",
        },
    )
