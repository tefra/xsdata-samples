from __future__ import annotations

from dataclasses import dataclass, field

from crossref.models.gov.nih.nlm.ncbi.jats1.article_id_pub_id_type import (
    ArticleIdPubIdType,
)

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass(kw_only=True)
class ArticleId:
    """
    <div> <h3>Article Identifier</h3> </div>.
    """

    class Meta:
        name = "article-id"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    assigning_authority: None | str = field(
        default=None,
        metadata={
            "name": "assigning-authority",
            "type": "Attribute",
        },
    )
    custom_type: None | str = field(
        default=None,
        metadata={
            "name": "custom-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    pub_id_type: None | ArticleIdPubIdType = field(
        default=None,
        metadata={
            "name": "pub-id-type",
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )
