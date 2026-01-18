from dataclasses import dataclass, field

from .font_size_enumeration import FontSizeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PrintPresentationStructure:
    colour: str | None = field(
        default=None,
        metadata={
            "name": "Colour",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    colour_name: str | None = field(
        default=None,
        metadata={
            "name": "ColourName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    colour_system: str | None = field(
        default=None,
        metadata={
            "name": "ColourSystem",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    background_colour: bytes | None = field(
        default=None,
        metadata={
            "name": "BackgroundColour",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_length": 6,
            "format": "base16",
        },
    )
    background_colour_name: str | None = field(
        default=None,
        metadata={
            "name": "BackgroundColourName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    text_colour: str | None = field(
        default=None,
        metadata={
            "name": "TextColour",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    text_colour_name: str | None = field(
        default=None,
        metadata={
            "name": "TextColourName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    text_font: str | None = field(
        default=None,
        metadata={
            "name": "TextFont",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    text_font_name: str | None = field(
        default=None,
        metadata={
            "name": "TextFontName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    text_language: str | None = field(
        default=None,
        metadata={
            "name": "TextLanguage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    font_size: FontSizeEnumeration | None = field(
        default=None,
        metadata={
            "name": "FontSize",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
