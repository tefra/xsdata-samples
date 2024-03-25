from dataclasses import dataclass, field
from typing import Tuple

from sdmx_ml.models.category_scheme_type import CategorySchemeType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class CategorySchemesType:
    """CategorySchemesType describes the structure of the category schemes
    container.

    It contains one or more category scheme, which can be explicitly
    detailed or referenced from an external structure document or
    registry service.

    :ivar category_scheme: CategoryScheme provides the details of a
        category scheme, which is the descriptive information for an
        arrangement or division of categories into groups based on
        characteristics, which the objects have in common. This provides
        for a simple, leveled hierarchy or categories.
    """

    category_scheme: Tuple[CategorySchemeType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "CategoryScheme",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "min_occurs": 1,
        },
    )
