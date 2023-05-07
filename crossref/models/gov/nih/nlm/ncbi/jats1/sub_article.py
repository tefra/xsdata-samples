from dataclasses import dataclass, field
from typing import List, Optional, Union
from crossref.models.gov.nih.nlm.ncbi.jats1.back import Back
from crossref.models.gov.nih.nlm.ncbi.jats1.body import Body
from crossref.models.gov.nih.nlm.ncbi.jats1.floats_group import FloatsGroup
from crossref.models.gov.nih.nlm.ncbi.jats1.front import Front
from crossref.models.gov.nih.nlm.ncbi.jats1.front_stub import FrontStub
from crossref.models.gov.nih.nlm.ncbi.jats1.processing_meta import ProcessingMeta
from crossref.models.gov.nih.nlm.ncbi.jats1.response import Response
from crossref.models.xml.lang_value import LangValue

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class SubArticle:
    """
    <div> <h3>Sub-Article</h3> </div>
    """
    class Meta:
        name = "sub-article"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    processing_meta: Optional[ProcessingMeta] = field(
        default=None,
        metadata={
            "name": "processing-meta",
            "type": "Element",
        }
    )
    front: Optional[Front] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    front_stub: Optional[FrontStub] = field(
        default=None,
        metadata={
            "name": "front-stub",
            "type": "Element",
        }
    )
    body: Optional[Body] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    back: Optional[Back] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    floats_group: Optional[FloatsGroup] = field(
        default=None,
        metadata={
            "name": "floats-group",
            "type": "Element",
        }
    )
    sub_article: List["SubArticle"] = field(
        default_factory=list,
        metadata={
            "name": "sub-article",
            "type": "Element",
        }
    )
    response: List[Response] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    article_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "article-type",
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
