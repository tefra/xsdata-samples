from dataclasses import dataclass, field
from typing import List, Optional
from crossref.models.gov.nih.nlm.ncbi.jats1.glyph_data import GlyphData
from crossref.models.gov.nih.nlm.ncbi.jats1.glyph_ref import GlyphRef
from crossref.models.gov.nih.nlm.ncbi.jats1.inline_graphic import InlineGraphic

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class PrivateChar:
    """
    <div> <h3>Private Character (Custom or Unicode)</h3> </div>
    """
    class Meta:
        name = "private-char"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    glyph_data: Optional[GlyphData] = field(
        default=None,
        metadata={
            "name": "glyph-data",
            "type": "Element",
        }
    )
    glyph_ref: Optional[GlyphRef] = field(
        default=None,
        metadata={
            "name": "glyph-ref",
            "type": "Element",
        }
    )
    inline_graphic: List[InlineGraphic] = field(
        default_factory=list,
        metadata={
            "name": "inline-graphic",
            "type": "Element",
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    name: Optional[str] = field(
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
