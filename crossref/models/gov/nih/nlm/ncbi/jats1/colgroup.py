from dataclasses import dataclass, field
from typing import List, Optional

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

    col: List[Col] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    align: Optional[ColgroupAlign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    char: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    charoff: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: Optional[str] = field(
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
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    valign: Optional[ColgroupValign] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    width: Optional[str] = field(
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
