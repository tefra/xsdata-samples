from __future__ import annotations

from dataclasses import dataclass

from sdmx_ml.models.representation_type import RepresentationType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"


@dataclass(frozen=True, kw_only=True)
class ConceptRepresentation(RepresentationType):
    """
    ConceptRepresentation defines the core representation that are allowed
    for a concept.

    The text format allowed for a concept is that which is allowed for any
    non-target object component.
    """
