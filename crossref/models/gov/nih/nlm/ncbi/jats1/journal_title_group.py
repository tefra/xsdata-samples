from dataclasses import dataclass, field
from typing import List, Optional
from crossref.models.gov.nih.nlm.ncbi.jats1.abbrev_journal_title import (
    AbbrevJournalTitle,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.journal_subtitle import (
    JournalSubtitle,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.journal_title import JournalTitle
from crossref.models.gov.nih.nlm.ncbi.jats1.trans_title_group import (
    TransTitleGroup,
)

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class JournalTitleGroup:
    """
    <div> <h3>Journal Title Group</h3> </div>
    """

    class Meta:
        name = "journal-title-group"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    journal_title: List[JournalTitle] = field(
        default_factory=list,
        metadata={
            "name": "journal-title",
            "type": "Element",
        },
    )
    journal_subtitle: List[JournalSubtitle] = field(
        default_factory=list,
        metadata={
            "name": "journal-subtitle",
            "type": "Element",
        },
    )
    trans_title_group: List[TransTitleGroup] = field(
        default_factory=list,
        metadata={
            "name": "trans-title-group",
            "type": "Element",
        },
    )
    abbrev_journal_title: List[AbbrevJournalTitle] = field(
        default_factory=list,
        metadata={
            "name": "abbrev-journal-title",
            "type": "Element",
        },
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
