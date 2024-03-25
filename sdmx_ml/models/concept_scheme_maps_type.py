from dataclasses import dataclass, field
from typing import Tuple

from sdmx_ml.models.concept_scheme_map_type import ConceptSchemeMapType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class ConceptSchemeMapsType:
    """ConceptSchemeMapsType describes the structure of the concept scheme maps
    container.

    It contains one or more concept scheme map, which can be explicitly
    detailed or referenced from an external structure document or
    registry service.

    :ivar concept_scheme_map: ConceptSchemeMap provides the details of a
        concept scheme map, which descibes mappings between concepts in
        different schemes.
    """

    concept_scheme_map: Tuple[ConceptSchemeMapType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ConceptSchemeMap",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "min_occurs": 1,
        },
    )
