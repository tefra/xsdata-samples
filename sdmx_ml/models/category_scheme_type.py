from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from sdmx_ml.models.item_scheme_type import ItemSchemeType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"


@dataclass(frozen=True, kw_only=True)
class CategorySchemeType(ItemSchemeType):
    """
    CategorySchemeType describes the structure of a category scheme.

    A category scheme is the descriptive information for an arrangement or
    division of categories into groups based on characteristics, which the
    objects have in common. This provides for a simple, leveled hierarchy
    or categories.
    """

    choice_1: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
