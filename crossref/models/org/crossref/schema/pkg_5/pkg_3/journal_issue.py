from __future__ import annotations

from dataclasses import dataclass, field

from crossref.models.org.crossref.schema.pkg_5.pkg_3.archive_locations import (
    ArchiveLocations,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.contributors import (
    Contributors,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.doi_data import DoiData
from crossref.models.org.crossref.schema.pkg_5.pkg_3.issue import Issue
from crossref.models.org.crossref.schema.pkg_5.pkg_3.journal_volume import (
    JournalVolume,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.publication_date import (
    PublicationDate,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.special_numbering import (
    SpecialNumbering,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.titles import Titles

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass(kw_only=True)
class JournalIssue:
    """
    Container for metadata that defines a single issue of a journal.
    """

    class Meta:
        name = "journal_issue"
        namespace = "http://www.crossref.org/schema/5.3.1"

    contributors: None | Contributors = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    titles: None | Titles = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    publication_date: list[PublicationDate] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 10,
        },
    )
    journal_volume: None | JournalVolume = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    issue: None | Issue = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    special_numbering: None | SpecialNumbering = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    archive_locations: None | ArchiveLocations = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    doi_data: None | DoiData = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
