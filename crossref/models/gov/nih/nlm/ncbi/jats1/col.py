from dataclasses import dataclass, field
from typing import Optional

from crossref.models.gov.nih.nlm.ncbi.jats1.col_align import ColAlign
from crossref.models.gov.nih.nlm.ncbi.jats1.col_valign import ColValign

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class Col:
    class Meta:
        name = "col"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    align: Optional[ColAlign] = field(
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
    valign: Optional[ColValign] = field(
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
