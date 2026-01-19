from __future__ import annotations

from dataclasses import dataclass

from sdmx_ml.models.item_type import ItemType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"


@dataclass(frozen=True, kw_only=True)
class Item(ItemType):
    """
    Item is an abstract element that serves as a substitution head for all
    items in an item scheme, including those items nested within other
    items.

    Concrete instances of this must use a concrete instance of ItemType.
    """

    class Meta:
        namespace = (
            "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"
        )
