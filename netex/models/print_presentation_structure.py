from dataclasses import dataclass, field
from typing import Optional
from .font_size_enumeration import FontSizeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PrintPresentationStructure:
    colour: Optional[str] = field(
        default=None,
        metadata={
            "name": "Colour",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    colour_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ColourName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    colour_system: Optional[str] = field(
        default=None,
        metadata={
            "name": "ColourSystem",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    background_colour: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "BackgroundColour",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_length": 6,
            "format": "base16",
        },
    )
    background_colour_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "BackgroundColourName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    text_colour: Optional[str] = field(
        default=None,
        metadata={
            "name": "TextColour",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    text_colour_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "TextColourName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    text_font: Optional[str] = field(
        default=None,
        metadata={
            "name": "TextFont",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    text_font_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "TextFontName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    text_language: Optional[str] = field(
        default=None,
        metadata={
            "name": "TextLanguage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    font_size: Optional[FontSizeEnumeration] = field(
        default=None,
        metadata={
            "name": "FontSize",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
