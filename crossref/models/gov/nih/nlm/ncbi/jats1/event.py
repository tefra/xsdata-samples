from dataclasses import dataclass, field
from typing import List, Optional, Union
from crossref.models.gov.nih.nlm.ncbi.jats1.annotation import Permissions
from crossref.models.gov.nih.nlm.ncbi.jats1.article_id import ArticleId
from crossref.models.gov.nih.nlm.ncbi.jats1.article_version import ArticleVersion
from crossref.models.gov.nih.nlm.ncbi.jats1.article_version_alternatives import ArticleVersionAlternatives
from crossref.models.gov.nih.nlm.ncbi.jats1.date import Date
from crossref.models.gov.nih.nlm.ncbi.jats1.event_desc import EventDesc
from crossref.models.gov.nih.nlm.ncbi.jats1.isbn import Isbn
from crossref.models.gov.nih.nlm.ncbi.jats1.issn import Issn
from crossref.models.gov.nih.nlm.ncbi.jats1.issn_l import IssnL
from crossref.models.gov.nih.nlm.ncbi.jats1.notes import Notes
from crossref.models.gov.nih.nlm.ncbi.jats1.pub_date import PubDate
from crossref.models.gov.nih.nlm.ncbi.jats1.pub_date_not_available import PubDateNotAvailable
from crossref.models.gov.nih.nlm.ncbi.jats1.self_uri import SelfUri
from crossref.models.xml.lang_value import LangValue

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class Event:
    """
    <div> <h3>Event in Publishing History</h3> </div>
    """
    class Meta:
        name = "event"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    event_desc: Optional[EventDesc] = field(
        default=None,
        metadata={
            "name": "event-desc",
            "type": "Element",
        }
    )
    article_id: List[ArticleId] = field(
        default_factory=list,
        metadata={
            "name": "article-id",
            "type": "Element",
        }
    )
    article_version: Optional[ArticleVersion] = field(
        default=None,
        metadata={
            "name": "article-version",
            "type": "Element",
        }
    )
    article_version_alternatives: Optional[ArticleVersionAlternatives] = field(
        default=None,
        metadata={
            "name": "article-version-alternatives",
            "type": "Element",
        }
    )
    pub_date: List[PubDate] = field(
        default_factory=list,
        metadata={
            "name": "pub-date",
            "type": "Element",
        }
    )
    pub_date_not_available: Optional[PubDateNotAvailable] = field(
        default=None,
        metadata={
            "name": "pub-date-not-available",
            "type": "Element",
        }
    )
    date: List[Date] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    issn: List[Issn] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    issn_l: Optional[IssnL] = field(
        default=None,
        metadata={
            "name": "issn-l",
            "type": "Element",
        }
    )
    isbn: List[Isbn] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    permissions: Optional[Permissions] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    notes: List[Notes] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    self_uri: List[SelfUri] = field(
        default_factory=list,
        metadata={
            "name": "self-uri",
            "type": "Element",
        }
    )
    event_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "event-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
