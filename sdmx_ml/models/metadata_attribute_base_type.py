from dataclasses import dataclass, field
from typing import Optional

from sdmx_ml.models.component_type import ComponentType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class MetadataAttributeBaseType(ComponentType):
    """
    MetadataAttributeBaseType is an abstract base type the serves as the basis for
    the MetadataAttributeType.
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
