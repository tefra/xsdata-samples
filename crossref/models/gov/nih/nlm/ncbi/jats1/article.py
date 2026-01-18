from dataclasses import dataclass, field
from typing import Optional, Union

from crossref.models.gov.nih.nlm.ncbi.jats1.article_dtd_version import (
    ArticleDtdVersion,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.back import Back
from crossref.models.gov.nih.nlm.ncbi.jats1.body import Body
from crossref.models.gov.nih.nlm.ncbi.jats1.floats_group import FloatsGroup
from crossref.models.gov.nih.nlm.ncbi.jats1.front import Front
from crossref.models.gov.nih.nlm.ncbi.jats1.processing_meta import (
    ProcessingMeta,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.response import Response
from crossref.models.gov.nih.nlm.ncbi.jats1.sub_article import SubArticle
from crossref.models.xml.lang_value import LangValue

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class Article:
    """
    <div> <h3>Article</h3> </div>.
    """

    class Meta:
        name = "article"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    processing_meta: ProcessingMeta | None = field(
        default=None,
        metadata={
            "name": "processing-meta",
            "type": "Element",
        },
    )
    front: Front | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    body: Body | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    back: Back | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    floats_group: FloatsGroup | None = field(
        default=None,
        metadata={
            "name": "floats-group",
            "type": "Element",
        },
    )
    sub_article: list[SubArticle] = field(
        default_factory=list,
        metadata={
            "name": "sub-article",
            "type": "Element",
        },
    )
    response: list[Response] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    article_type: str | None = field(
        default=None,
        metadata={
            "name": "article-type",
            "type": "Attribute",
        },
    )
    dtd_version: ArticleDtdVersion | None = field(
        default=None,
        metadata={
            "name": "dtd-version",
            "type": "Attribute",
        },
    )
    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: str | None = field(
        default=None,
        metadata={
            "name": "specific-use",
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
    lang: str | LangValue = field(
        default="en",
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
