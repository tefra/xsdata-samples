from __future__ import annotations

from dataclasses import dataclass, field

from crossref.models.gov.nih.nlm.ncbi.jats1.col_align import ColAlign
from crossref.models.gov.nih.nlm.ncbi.jats1.col_valign import ColValign

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class Col:
    class Meta:
        name = "col"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    align: ColAlign | None = field(
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
    valign: ColValign | None = field(
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
