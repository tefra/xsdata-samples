from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.concept_scheme_type import ConceptSchemeType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"


@dataclass(frozen=True, kw_only=True)
class ConceptSchemesType:
    """
    ConceptSchemesType describes the structure of the concept schemes
    container.

    It contains one or more concept schemes, which can be explicitly
    detailed or referenced from an external structure document or registry
    service.

    :ivar concept_scheme: ConceptScheme provides the details of a
        concept scheme, which is the descriptive information for an
        arrangement or division of concepts into groups based on
        characteristics, which the objects have in common. It contains a
        collection of concept definitions, that may be arranged in
        simple hierarchies.
    """

    concept_scheme: tuple[ConceptSchemeType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ConceptScheme",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure",
        },
    )
