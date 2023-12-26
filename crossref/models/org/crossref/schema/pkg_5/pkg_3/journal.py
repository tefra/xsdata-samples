from dataclasses import dataclass, field
from typing import List, Optional
from crossref.models.org.crossref.schema.pkg_5.pkg_3.journal_article import (
    JournalArticle,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.journal_issue import (
    JournalIssue,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.journal_metadata import (
    JournalMetadata,
)

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class Journal:
    """Container for all information about a single journal and the volumes,
    issues, and articles being registered within the journal.

    Within a journal instance you may register articles from a single
    issue, detailed in journal_issue. If you want to register items from
    more than one issue you must use multiple journal instances within
    your XML file.
    """

    class Meta:
        name = "journal"
        namespace = "http://www.crossref.org/schema/5.3.1"

    journal_metadata: Optional[JournalMetadata] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    journal_issue: Optional[JournalIssue] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    journal_article: List[JournalArticle] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
