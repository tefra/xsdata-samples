from __future__ import annotations

from dataclasses import dataclass

from sdmx_ml.models.item_scheme_map_type import ItemSchemeMapType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class CategorySchemeMapType(ItemSchemeMapType):
    """
    CategorySchemeMapType defines the structure of a map which identifies
    relationships between categories in different category schemes.
    """
