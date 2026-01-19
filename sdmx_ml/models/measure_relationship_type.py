from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"


@dataclass(frozen=True, kw_only=True)
class MeasureRelationshipType:
    """
    MeasureRelationshipType allows for the description of an attribute's
    relationship to one or more measures.

    :ivar measure: This is a reference to a measure defined in this data
        structure definition.
    """

    measure: tuple[str, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Measure",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure",
            "min_occurs": 1,
            "pattern": r"[A-Za-z][A-Za-z0-9_\-]*",
        },
    )
