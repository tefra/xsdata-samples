from dataclasses import dataclass, field
from typing import Optional

from sdmx_ml.models.item_scheme_map_base_type import ItemSchemeMapBaseType
from sdmx_ml.models.single_value_mapping_type import SingleValueMappingType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class ItemSchemeMapType(ItemSchemeMapBaseType):
    """
    ItemSchemeMapType is an abstract base type which forms the basis for
    mapping items between item schemes of the same type.

    :ivar source: Source provides a reference to the item scheme which
        items are mapped from.
    :ivar target: Target provides a reference to the item scheme which
        items are mapped to.
    :ivar item_map:
    """

    source: str | None = field(
        default=None,
        metadata={
            "name": "Source",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "required": True,
            "pattern": r".+\)",
        },
    )
    target: str | None = field(
        default=None,
        metadata={
            "name": "Target",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "required": True,
            "pattern": r".+\)",
        },
    )
    item_map: tuple[SingleValueMappingType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ItemMap",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
