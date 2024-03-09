from dataclasses import dataclass, field
from typing import List, Optional
from crossref.models.gov.nih.nlm.ncbi.jats1.abbrev import (
    AltTitle,
    ArticleTitle,
    FnGroup,
    Subtitle,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.trans_title_group import (
    TransTitleGroup,
)

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class TitleGroup:
    """
    <div> <h3>Title Group</h3> </div>
    """

    class Meta:
        name = "title-group"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    article_title: Optional[ArticleTitle] = field(
        default=None,
        metadata={
            "name": "article-title",
            "type": "Element",
            "required": True,
        },
    )
    subtitle: List[Subtitle] = field(
        default_factory=list,
        metadata={
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
    alt_title: List[AltTitle] = field(
        default_factory=list,
        metadata={
            "name": "alt-title",
            "type": "Element",
        },
    )
    fn_group: Optional[FnGroup] = field(
        default=None,
        metadata={
            "name": "fn-group",
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
