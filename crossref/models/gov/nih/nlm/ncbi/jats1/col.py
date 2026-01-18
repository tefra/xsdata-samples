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

    align: None | ColAlign = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    char: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    charoff: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
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
    style: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    valign: None | ColValign = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    width: None | str = field(
        default=None,
        metadata={
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
