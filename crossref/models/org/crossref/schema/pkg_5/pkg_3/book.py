from __future__ import annotations

from dataclasses import dataclass, field

from crossref.models.org.crossref.schema.pkg_5.pkg_3.book_book_type import (
    BookBookType,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.book_metadata import (
    BookMetadata,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.book_series_metadata import (
    BookSeriesMetadata,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.book_set_metadata import (
    BookSetMetadata,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.content_item import (
    ContentItem,
)

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class Book:
    """
    Container for all information about a single book.
    """

    class Meta:
        name = "book"
        namespace = "http://www.crossref.org/schema/5.3.1"

    book_metadata: None | BookMetadata = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    book_series_metadata: None | BookSeriesMetadata = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    book_set_metadata: None | BookSetMetadata = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    content_item: list[ContentItem] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    book_type: None | BookBookType = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
