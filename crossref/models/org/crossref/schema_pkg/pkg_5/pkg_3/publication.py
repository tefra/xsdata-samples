from dataclasses import dataclass, field
from typing import List, Optional
from crossref.models.org.crossref.schema_pkg.pkg_5.pkg_3.isbn import Isbn
from crossref.models.org.crossref.schema_pkg.pkg_5.pkg_3.issn import Issn

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

    full_title: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 10,
            "min_length": 1,
            "max_length": 255,
        }
    )
    issn: List[Issn] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
        }
    )
    isbn: List[Isbn] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 2,
        }
    )
    doi: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 6,
            "max_length": 2048,
            "pattern": r"10\.[0-9]{4,9}/.{1,200}",
        }
    )
