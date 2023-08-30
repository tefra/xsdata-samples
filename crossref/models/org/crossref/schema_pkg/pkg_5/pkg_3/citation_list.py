from dataclasses import dataclass, field
from typing import List
from crossref.models.org.crossref.schema_pkg.pkg_5.pkg_3.citation import Citation

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class CitationList:
    """
    A list of articles, books, and other content cited by the item being
    registered.
    """
    class Meta:
        name = "citation_list"
        namespace = "http://www.crossref.org/schema/5.3.1"

    citation: List[Citation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
