from dataclasses import dataclass, field
from typing import Optional

from crossref.models.gov.nih.nlm.ncbi.jats1.abbrev import (
    Aff,
    AffAlternatives,
    ContribGroup,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.isbn import Isbn
from crossref.models.gov.nih.nlm.ncbi.jats1.issn import Issn
from crossref.models.gov.nih.nlm.ncbi.jats1.issn_l import IssnL
from crossref.models.gov.nih.nlm.ncbi.jats1.journal_id import JournalId
from crossref.models.gov.nih.nlm.ncbi.jats1.journal_title_group import (
    JournalTitleGroup,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.notes import Notes
from crossref.models.gov.nih.nlm.ncbi.jats1.publisher import Publisher
from crossref.models.gov.nih.nlm.ncbi.jats1.self_uri import SelfUri

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class JournalMeta:
    """
    <div> <h3>Journal Metadata</h3> </div>
    """

    class Meta:
        name = "journal-meta"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    journal_id: list[JournalId] = field(
        default_factory=list,
        metadata={
            "name": "journal-id",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    journal_title_group: list[JournalTitleGroup] = field(
        default_factory=list,
        metadata={
            "name": "journal-title-group",
            "type": "Element",
        },
    )
    contrib_group: list[ContribGroup] = field(
        default_factory=list,
        metadata={
            "name": "contrib-group",
            "type": "Element",
        },
    )
    aff: list[Aff] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    aff_alternatives: list[AffAlternatives] = field(
        default_factory=list,
        metadata={
            "name": "aff-alternatives",
            "type": "Element",
        },
    )
    issn: list[Issn] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    issn_l: Optional[IssnL] = field(
        default=None,
        metadata={
            "name": "issn-l",
            "type": "Element",
        },
    )
    isbn: list[Isbn] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    publisher: Optional[Publisher] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    notes: list[Notes] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    self_uri: list[SelfUri] = field(
        default_factory=list,
        metadata={
            "name": "self-uri",
            "type": "Element",
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
