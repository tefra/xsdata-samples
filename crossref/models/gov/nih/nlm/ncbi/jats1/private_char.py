from __future__ import annotations

from dataclasses import dataclass, field

from crossref.models.gov.nih.nlm.ncbi.jats1.glyph_data import GlyphData
from crossref.models.gov.nih.nlm.ncbi.jats1.glyph_ref import GlyphRef
from crossref.models.gov.nih.nlm.ncbi.jats1.inline_graphic import InlineGraphic

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class PrivateChar:
    """
    <div> <h3>Private Character (Custom or Unicode)</h3> </div>.
    """

    class Meta:
        name = "private-char"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    glyph_data: GlyphData | None = field(
        default=None,
        metadata={
            "name": "glyph-data",
            "type": "Element",
        },
    )
    glyph_ref: GlyphRef | None = field(
        default=None,
        metadata={
            "name": "glyph-ref",
            "type": "Element",
        },
    )
    inline_graphic: list[InlineGraphic] = field(
        default_factory=list,
        metadata={
            "name": "inline-graphic",
            "type": "Element",
        },
    )
    description: str | None = field(
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
    name: str | None = field(
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
