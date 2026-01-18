from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class ItemNumber:
    """
    A publisher-assigned number that uniquely identifies the item being
    registered.
    """

    class Meta:
        name = "item_number"
        namespace = "http://www.crossref.org/schema/5.3.1"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
            "max_length": 32,
        },
    )
    item_number_type: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
