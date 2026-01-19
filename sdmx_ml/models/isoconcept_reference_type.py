from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"


@dataclass(frozen=True, kw_only=True)
class IsoconceptReferenceType:
    """
    ISOConceptReferenceType provides a reference to and ISO 11179 concept.
    """

    class Meta:
        name = "ISOConceptReferenceType"

    concept_agency: str = field(
        metadata={
            "name": "ConceptAgency",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure",
            "required": True,
        }
    )
    concept_scheme_id: str = field(
        metadata={
            "name": "ConceptSchemeID",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure",
            "required": True,
        }
    )
    concept_id: str = field(
        metadata={
            "name": "ConceptID",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure",
            "required": True,
        }
    )
