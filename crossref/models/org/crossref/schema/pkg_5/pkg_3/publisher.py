from __future__ import annotations

from dataclasses import dataclass, field

from crossref.models.org.crossref.schema.pkg_5.pkg_3.publisher_name import (
    PublisherName,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.publisher_place import (
    PublisherPlace,
)

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class Publisher:
    """
    A container for information about the publisher of the item being
    registered.
    """

    class Meta:
        name = "publisher"
        namespace = "http://www.crossref.org/schema/5.3.1"

    publisher_name: PublisherName | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    publisher_place: PublisherPlace | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
