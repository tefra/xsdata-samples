from __future__ import annotations

from dataclasses import dataclass, field

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

    fontchar: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    fontname: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    format: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    resolution: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    x_size: None | str = field(
        default=None,
        metadata={
            "name": "x-size",
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
    space: SpaceValue = field(
        init=False,
        default=SpaceValue.PRESERVE,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    y_size: None | str = field(
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
