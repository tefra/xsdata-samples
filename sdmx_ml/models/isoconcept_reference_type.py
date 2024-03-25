from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class IsoconceptReferenceType:
    """
    ISOConceptReferenceType provides a reference to and ISO 11179 concept.
    """

    class Meta:
        name = "ISOConceptReferenceType"

    concept_agency: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConceptAgency",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "required": True,
        },
    )
    concept_scheme_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConceptSchemeID",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "required": True,
        },
    )
    concept_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConceptID",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "required": True,
        },
    )
