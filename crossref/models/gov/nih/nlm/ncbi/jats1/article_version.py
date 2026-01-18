from dataclasses import dataclass, field
from typing import Optional

from crossref.models.xlink.actuate_type import ActuateType
from crossref.models.xlink.show_type import ShowType
from crossref.models.xlink.type_type import TypeType

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class ArticleVersion:
    """
    <div> <h3>Article Version</h3> </div>.
    """

    class Meta:
        name = "article-version"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    article_version_type: str | None = field(
        default=None,
        metadata={
            "name": "article-version-type",
            "type": "Attribute",
        },
    )
    assigning_authority: str | None = field(
        default=None,
        metadata={
            "name": "assigning-authority",
            "type": "Attribute",
        },
    )
    content_type: str | None = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    designator: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    hreflang: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    iso_8601_date: str | None = field(
        default=None,
        metadata={
            "name": "iso-8601-date",
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
    vocab: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    vocab_identifier: str | None = field(
        default=None,
        metadata={
            "name": "vocab-identifier",
            "type": "Attribute",
        },
    )
    vocab_term: str | None = field(
        default=None,
        metadata={
            "name": "vocab-term",
            "type": "Attribute",
        },
    )
    vocab_term_identifier: str | None = field(
        default=None,
        metadata={
            "name": "vocab-term-identifier",
            "type": "Attribute",
        },
    )
    actuate: ActuateType | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    show: ShowType | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    title: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    type_value: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    base: str | None = field(
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
