from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.component_type import ComponentType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"


@dataclass(frozen=True, kw_only=True)
class MeasureBaseType(ComponentType):
    """
    MeasureBaseType is an abstract base type that refines ComponentType to
    restrict the representations to those which are applicable for a
    measure.
    """

    concept_identity: str = field(
        metadata={
            "name": "ConceptIdentity",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure",
            "required": True,
            "pattern": r".+\.conceptscheme\.Concept=.+",
        }
    )
