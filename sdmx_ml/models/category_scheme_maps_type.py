from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.category_scheme_map_type import CategorySchemeMapType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"


@dataclass(frozen=True, kw_only=True)
class CategorySchemeMapsType:
    """
    CategorySchemeMapsType describes the structure of the category scheme
    maps container.

    It contains one or more category scheme map, which can be explicitly
    detailed or referenced from an external structure document or registry
    service.

    :ivar category_scheme_map: CategorySchemeMap provides the details of
        a category scheme map, which describes mappings between
        categories in different schemes.
    """

    category_scheme_map: tuple[CategorySchemeMapType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "CategorySchemeMap",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure",
            "min_occurs": 1,
        },
    )
