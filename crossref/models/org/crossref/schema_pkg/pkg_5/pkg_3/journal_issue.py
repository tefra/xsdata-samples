from dataclasses import dataclass, field
from typing import List, Optional
from crossref.models.org.crossref.schema_pkg.pkg_5.pkg_3.archive_locations import ArchiveLocations
from crossref.models.org.crossref.schema_pkg.pkg_5.pkg_3.contributors import Contributors
from crossref.models.org.crossref.schema_pkg.pkg_5.pkg_3.doi_data import DoiData
from crossref.models.org.crossref.schema_pkg.pkg_5.pkg_3.journal_volume import JournalVolume
from crossref.models.org.crossref.schema_pkg.pkg_5.pkg_3.publication_date import PublicationDate
from crossref.models.org.crossref.schema_pkg.pkg_5.pkg_3.titles import Titles

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class JournalIssue:
    """
    Container for metadata that defines a single issue of a journal.
    """
    class Meta:
        name = "journal_issue"
        namespace = "http://www.crossref.org/schema/5.3.1"

    contributors: Optional[Contributors] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    titles: Optional[Titles] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    publication_date: List[PublicationDate] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 10,
        }
    )
    journal_volume: Optional[JournalVolume] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    issue: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 1,
            "max_length": 32,
        }
    )
    special_numbering: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 1,
            "max_length": 15,
        }
    )
    archive_locations: Optional[ArchiveLocations] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    doi_data: Optional[DoiData] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
