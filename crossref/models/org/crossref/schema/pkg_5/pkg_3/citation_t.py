from dataclasses import dataclass, field
from typing import Optional

from crossref.models.org.crossref.schema.pkg_5.pkg_3.article_title import (
    ArticleTitle,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.author import Author
from crossref.models.org.crossref.schema.pkg_5.pkg_3.c_year import CYear
from crossref.models.org.crossref.schema.pkg_5.pkg_3.component_number import (
    ComponentNumber,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.doi import Doi
from crossref.models.org.crossref.schema.pkg_5.pkg_3.edition_number import (
    EditionNumber,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.elocation_id import (
    ElocationId,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.first_page import (
    FirstPage,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.isbn import Isbn
from crossref.models.org.crossref.schema.pkg_5.pkg_3.issn import Issn
from crossref.models.org.crossref.schema.pkg_5.pkg_3.issue import Issue
from crossref.models.org.crossref.schema.pkg_5.pkg_3.journal_title import (
    JournalTitle,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.series_title import (
    SeriesTitle,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.standards_body import (
    StandardsBody,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.std_designator import (
    StdDesignator,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.unstructured_citation import (
    UnstructuredCitation,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.volume import Volume
from crossref.models.org.crossref.schema.pkg_5.pkg_3.volume_title import (
    VolumeTitle,
)

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class CitationT:
    class Meta:
        name = "citation_t"

    issn: Issn | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.crossref.org/schema/5.3.1",
        },
    )
    journal_title: JournalTitle | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.crossref.org/schema/5.3.1",
        },
    )
    author: Author | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.crossref.org/schema/5.3.1",
        },
    )
    volume: Volume | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.crossref.org/schema/5.3.1",
        },
    )
    issue: Issue | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.crossref.org/schema/5.3.1",
        },
    )
    first_page: FirstPage | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.crossref.org/schema/5.3.1",
        },
    )
    elocation_id: ElocationId | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.crossref.org/schema/5.3.1",
        },
    )
    c_year: CYear | None = field(
        default=None,
        metadata={
            "name": "cYear",
            "type": "Element",
            "namespace": "http://www.crossref.org/schema/5.3.1",
        },
    )
    doi: Doi | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.crossref.org/schema/5.3.1",
        },
    )
    isbn: Isbn | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.crossref.org/schema/5.3.1",
        },
    )
    series_title: SeriesTitle | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.crossref.org/schema/5.3.1",
        },
    )
    volume_title: VolumeTitle | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.crossref.org/schema/5.3.1",
        },
    )
    edition_number: EditionNumber | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.crossref.org/schema/5.3.1",
        },
    )
    component_number: ComponentNumber | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.crossref.org/schema/5.3.1",
        },
    )
    article_title: ArticleTitle | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.crossref.org/schema/5.3.1",
        },
    )
    std_designator: StdDesignator | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.crossref.org/schema/5.3.1",
        },
    )
    standards_body: StandardsBody | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.crossref.org/schema/5.3.1",
        },
    )
    unstructured_citation: UnstructuredCitation | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.crossref.org/schema/5.3.1",
        },
    )
