from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.component_type import ComponentType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class AttributeBaseType(ComponentType):
    """
    AttributeBaseType is an abstract base type that serves as the basis for
    the AttributeType.

    It restricts the text format base to a text format valid for data
    components (that does not allow for XHTML representation). The local
    representation is restricted to the values defined in codelist. The
    concept role is restricted to the values valid for a data attribute.
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
