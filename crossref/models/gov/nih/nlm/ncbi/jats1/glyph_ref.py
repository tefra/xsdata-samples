from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class GlyphRef:
    """
    <div> <h3>Glyph Reference For a Private Character</h3> </div>
    """

    class Meta:
        name = "glyph-ref"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    glyph_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "glyph-data",
            "type": "Attribute",
        },
    )
    id: Optional[str] = field(
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
