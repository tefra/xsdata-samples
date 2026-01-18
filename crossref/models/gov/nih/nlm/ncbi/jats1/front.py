from __future__ import annotations

from dataclasses import dataclass, field

from crossref.models.gov.nih.nlm.ncbi.jats1.article_meta import ArticleMeta
from crossref.models.gov.nih.nlm.ncbi.jats1.journal_meta import JournalMeta
from crossref.models.gov.nih.nlm.ncbi.jats1.notes import Notes

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class Front:
    """
    <div> <h3>Front Matter</h3> </div>.
    """

    class Meta:
        name = "front"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    journal_meta: JournalMeta | None = field(
        default=None,
        metadata={
            "name": "journal-meta",
            "type": "Element",
            "required": True,
        },
    )
    article_meta: ArticleMeta | None = field(
        default=None,
        metadata={
            "name": "article-meta",
            "type": "Element",
            "required": True,
        },
    )
    notes: Notes | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    base: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
