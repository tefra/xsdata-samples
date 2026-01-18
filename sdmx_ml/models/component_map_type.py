from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.annotable_type import AnnotableType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class ComponentMapType(AnnotableType):
    """
    ComponentMapType defines the structure for relating a component in a
    source structure to a component in a target structure.
    """

    source: tuple[str, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Source",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "min_occurs": 1,
            "pattern": r"[A-Za-z0-9_@$\-]+",
        },
    )
    target: tuple[str, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Target",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "min_occurs": 1,
            "pattern": r"[A-Za-z0-9_@$\-]+",
        },
    )
    representation_map: str | None = field(
        default=None,
        metadata={
            "name": "RepresentationMap",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "pattern": r".+\.structuremapping\.RepresentationMap=.+",
        },
    )
