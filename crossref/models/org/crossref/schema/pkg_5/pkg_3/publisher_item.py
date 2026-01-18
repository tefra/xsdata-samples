from __future__ import annotations

from dataclasses import dataclass, field

from crossref.models.org.crossref.schema.pkg_5.pkg_3.identifier import (
    Identifier,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.item_number import (
    ItemNumber,
)

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class PublisherItem:
    """
    A container for item identification numbers set by a publisher.
    """

    class Meta:
        name = "publisher_item"
        namespace = "http://www.crossref.org/schema/5.3.1"

    item_number: list[ItemNumber] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 3,
        },
    )
    identifier: list[Identifier] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 10,
        },
    )
