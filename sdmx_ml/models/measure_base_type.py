from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.component_type import ComponentType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class MeasureBaseType(ComponentType):
    """
    MeasureBaseType is an abstract base type that refines ComponentType to
    rerstrict the represenations to those which are applicable for a
    measure.
    """

    concept_identity: None | str = field(
        default=None,
        metadata={
            "name": "ConceptIdentity",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "required": True,
            "pattern": r".+\.conceptscheme\.Concept=.+",
        },
    )
