from dataclasses import dataclass, field
from typing import Optional
from crossref.models.gov.nih.nlm.ncbi.jats1.article_meta import ArticleMeta
from crossref.models.gov.nih.nlm.ncbi.jats1.journal_meta import JournalMeta
from crossref.models.gov.nih.nlm.ncbi.jats1.notes import Notes

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class Front:
    """
    <div> <h3>Front Matter</h3> </div>
    """

    class Meta:
        name = "front"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    journal_meta: Optional[JournalMeta] = field(
        default=None,
        metadata={
            "name": "journal-meta",
            "type": "Element",
            "required": True,
        },
    )
    article_meta: Optional[ArticleMeta] = field(
        default=None,
        metadata={
            "name": "article-meta",
            "type": "Element",
            "required": True,
        },
    )
    notes: Optional[Notes] = field(
        default=None,
        metadata={
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
