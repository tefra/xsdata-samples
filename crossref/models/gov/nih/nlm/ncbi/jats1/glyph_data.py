from dataclasses import dataclass, field
from typing import Optional

from crossref.models.xml.space_value import SpaceValue

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class GlyphData:
    """
    <div> <h3>Glyph Data For a Private Character</h3> </div>.
    """

    class Meta:
        name = "glyph-data"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    fontchar: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    fontname: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    format: str | None = field(
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
    resolution: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    x_size: str | None = field(
        default=None,
        metadata={
            "name": "x-size",
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
    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    y_size: str | None = field(
        default=None,
        metadata={
            "name": "y-size",
            "type": "Attribute",
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
