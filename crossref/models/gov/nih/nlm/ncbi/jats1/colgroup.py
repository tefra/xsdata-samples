from dataclasses import dataclass, field
from typing import Optional

from crossref.models.gov.nih.nlm.ncbi.jats1.col import Col
from crossref.models.gov.nih.nlm.ncbi.jats1.colgroup_align import ColgroupAlign
from crossref.models.gov.nih.nlm.ncbi.jats1.colgroup_valign import (
    ColgroupValign,
)

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class Colgroup:
    class Meta:
        name = "colgroup"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    col: list[Col] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    align: ColgroupAlign | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    char: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    charoff: str | None = field(
        default=None,
        metadata={
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
    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    span: str = field(
        default="1",
        metadata={
            "type": "Attribute",
        },
    )
    style: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    valign: ColgroupValign | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    width: str | None = field(
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
