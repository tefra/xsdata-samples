from dataclasses import dataclass, field
from typing import List
from crossref.models.org.crossref.schema_pkg.pkg_5.pkg_3.book import Book
from crossref.models.org.crossref.schema_pkg.pkg_5.pkg_3.conference import Conference
from crossref.models.org.crossref.schema_pkg.pkg_5.pkg_3.database import Database
from crossref.models.org.crossref.schema_pkg.pkg_5.pkg_3.dissertation import Dissertation
from crossref.models.org.crossref.schema_pkg.pkg_5.pkg_3.journal import Journal
from crossref.models.org.crossref.schema_pkg.pkg_5.pkg_3.peer_review import PeerReview
from crossref.models.org.crossref.schema_pkg.pkg_5.pkg_3.pending_publication import PendingPublication
from crossref.models.org.crossref.schema_pkg.pkg_5.pkg_3.posted_content import PostedContent
from crossref.models.org.crossref.schema_pkg.pkg_5.pkg_3.report_paper import ReportPaper
from crossref.models.org.crossref.schema_pkg.pkg_5.pkg_3.sa_component import SaComponent
from crossref.models.org.crossref.schema_pkg.pkg_5.pkg_3.standard import Standard

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class Body:
    """Container for the main body of a DOI record submission.

    While it is possible to include records for multiple journals,
    books, conferences, or other types of content in a single
    submission, it is not possible to mix content types within a single
    DOI submission.
    """
    class Meta:
        name = "body"
        namespace = "http://www.crossref.org/schema/5.3.1"

    journal: List[Journal] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    book: List[Book] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    conference: List[Conference] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    sa_component: List[SaComponent] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    dissertation: List[Dissertation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    report_paper: List[ReportPaper] = field(
        default_factory=list,
        metadata={
            "name": "report-paper",
            "type": "Element",
        }
    )
    standard: List[Standard] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    database: List[Database] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    peer_review: List[PeerReview] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    pending_publication: List[PendingPublication] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    posted_content: List[PostedContent] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
