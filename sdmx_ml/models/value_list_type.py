from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.value_item_type import ValueItemType
from sdmx_ml.models.value_list_base_type import ValueListBaseType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True, kw_only=True)
class ValueListType(ValueListBaseType):
    """
    ValueListType defines the structure of value list.

    These represent a closed set of values the can occur for a dimension,
    measure, or attribute. These may be values, or values with names and
    descriptions (similar to a codelist).
    """

    value_item: tuple[ValueItemType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ValueItem",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
