from dataclasses import dataclass, field
from typing import List, Optional
from crossref.models.org.crossref.schema.pkg_5.pkg_3.doi import Doi
from crossref.models.org.crossref.schema.pkg_5.pkg_3.full_title import (
    FullTitle,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.isbn import Isbn
from crossref.models.org.crossref.schema.pkg_5.pkg_3.issn import Issn

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class Publication:
    """Used to define a publication (book, journal, etc) for pending publication
    content.

    A title must be supplied, as well as an ISSN, ISBN, or title-level
    DOI
    """

    class Meta:
        name = "publication"
        namespace = "http://www.crossref.org/schema/5.3.1"

    full_title: List[FullTitle] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 10,
        },
    )
    issn: List[Issn] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
        },
    )
    isbn: List[Isbn] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
        },
    )
    doi: Optional[Doi] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
