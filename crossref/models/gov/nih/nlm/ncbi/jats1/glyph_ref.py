from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class GlyphRef:
    """
    <div> <h3>Glyph Reference For a Private Character</h3> </div>.
    """

    class Meta:
        name = "glyph-ref"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    glyph_data: None | str = field(
        default=None,
        metadata={
            "name": "glyph-data",
            "type": "Attribute",
        },
    )
    id: None | str = field(
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
