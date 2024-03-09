from dataclasses import dataclass, field
from typing import List, Optional, Union

from crossref.models.gov.nih.nlm.ncbi.jats1.abbrev import ExtLink
from crossref.models.gov.nih.nlm.ncbi.jats1.article_id import ArticleId
from crossref.models.gov.nih.nlm.ncbi.jats1.article_version import (
    ArticleVersion,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.article_version_alternatives import (
    ArticleVersionAlternatives,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.date import Date
from crossref.models.gov.nih.nlm.ncbi.jats1.email import Email
from crossref.models.gov.nih.nlm.ncbi.jats1.isbn import Isbn
from crossref.models.gov.nih.nlm.ncbi.jats1.issn import Issn
from crossref.models.gov.nih.nlm.ncbi.jats1.issn_l import IssnL
from crossref.models.gov.nih.nlm.ncbi.jats1.pub_date import PubDate
from crossref.models.gov.nih.nlm.ncbi.jats1.pub_date_not_available import (
    PubDateNotAvailable,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.string_date import StringDate
from crossref.models.gov.nih.nlm.ncbi.jats1.uri import Uri
from crossref.models.xml.lang_value import LangValue

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class EventDesc:
    """
    <div> <h3>Event Description</h3> </div>
    """

    class Meta:
        name = "event-desc"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
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
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "email",
                    "type": Email,
                },
                {
                    "name": "ext-link",
                    "type": ExtLink,
                },
                {
                    "name": "uri",
                    "type": Uri,
                },
                {
                    "name": "article-id",
                    "type": ArticleId,
                },
                {
                    "name": "issn",
                    "type": Issn,
                },
                {
                    "name": "issn-l",
                    "type": IssnL,
                },
                {
                    "name": "isbn",
                    "type": Isbn,
                },
                {
                    "name": "article-version",
                    "type": ArticleVersion,
                },
                {
                    "name": "article-version-alternatives",
                    "type": ArticleVersionAlternatives,
                },
                {
                    "name": "date",
                    "type": Date,
                },
                {
                    "name": "string-date",
                    "type": StringDate,
                },
                {
                    "name": "pub-date",
                    "type": PubDate,
                },
                {
                    "name": "pub-date-not-available",
                    "type": PubDateNotAvailable,
                },
            ),
        },
    )
