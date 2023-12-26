from dataclasses import dataclass, field
from typing import Optional
from crossref.models.org.crossref.schema.pkg_5.pkg_3.isbn import Isbn
from crossref.models.org.crossref.schema.pkg_5.pkg_3.issn import Issn
from crossref.models.org.crossref.schema.pkg_5.pkg_3.standards_body import (
    StandardsBody,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.unstructured_citation import (
    UnstructuredCitation,
)

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class CitationT:
    class Meta:
        name = "citation_t"

    issn: Optional[Issn] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.crossref.org/schema/5.3.1",
        },
    )
    journal_title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.crossref.org/schema/5.3.1",
        },
    )
    author: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.crossref.org/schema/5.3.1",
        },
    )
    volume: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.crossref.org/schema/5.3.1",
            "min_length": 1,
            "max_length": 32,
        },
    )
    issue: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.crossref.org/schema/5.3.1",
            "min_length": 1,
            "max_length": 32,
        },
    )
    first_page: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.crossref.org/schema/5.3.1",
            "min_length": 1,
            "max_length": 32,
        },
    )
    elocation_id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.crossref.org/schema/5.3.1",
        },
    )
    c_year: Optional[str] = field(
        default=None,
        metadata={
            "name": "cYear",
            "type": "Element",
            "namespace": "http://www.crossref.org/schema/5.3.1",
        },
    )
    doi: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.crossref.org/schema/5.3.1",
            "min_length": 6,
            "max_length": 2048,
            "pattern": r"10\.[0-9]{4,9}/.{1,200}",
        },
    )
    isbn: Optional[Isbn] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.crossref.org/schema/5.3.1",
        },
    )
    series_title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.crossref.org/schema/5.3.1",
        },
    )
    volume_title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.crossref.org/schema/5.3.1",
        },
    )
    edition_number: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.crossref.org/schema/5.3.1",
            "min_length": 1,
            "max_length": 15,
        },
    )
    component_number: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.crossref.org/schema/5.3.1",
            "min_length": 1,
            "max_length": 50,
        },
    )
    article_title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.crossref.org/schema/5.3.1",
        },
    )
    std_designator: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.crossref.org/schema/5.3.1",
            "min_length": 2,
            "max_length": 150,
        },
    )
    standards_body: Optional[StandardsBody] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.crossref.org/schema/5.3.1",
        },
    )
    unstructured_citation: Optional[UnstructuredCitation] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.crossref.org/schema/5.3.1",
        },
    )
