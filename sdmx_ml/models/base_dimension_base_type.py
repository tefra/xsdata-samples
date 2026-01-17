from dataclasses import dataclass, field
from typing import Optional

from sdmx_ml.models.component_type import ComponentType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class BaseDimensionBaseType(ComponentType):
    """
    BaseDimensionBaseType is an abstract base type that serves as the basis
    for any dimension.

    It restricts the text format base to a text format valid for data
    components (that does not allow for XHTML representation).
    """

    concept_identity: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConceptIdentity",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "required": True,
            "pattern": r".+\.conceptscheme\.Concept=.+",
        },
    )
