from dataclasses import dataclass, field
from typing import List, Optional

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

    book_metadata: Optional[BookMetadata] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    book_series_metadata: Optional[BookSeriesMetadata] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    book_set_metadata: Optional[BookSetMetadata] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    content_item: List[ContentItem] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    book_type: Optional[BookBookType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
