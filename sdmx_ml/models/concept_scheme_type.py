from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from sdmx_ml.models.item_scheme_type import ItemSchemeType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class ConceptSchemeType(ItemSchemeType):
    """
    ConceptSchemeType describes the structure of a concept scheme.

    A concept scheme is the descriptive information for an arrangement or
    division of concepts into groups based on characteristics, which the
    objects have in common. It contains a collection of concept
    definitions, that may be arranged in simple hierarchies.
    """

    choice_1: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
