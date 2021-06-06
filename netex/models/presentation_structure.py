from dataclasses import dataclass, field
from typing import Optional
from .info_links_rel_structure import InfoLinksRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PresentationStructure:
    colour: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Colour",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_length": 6,
            "format": "base16",
        }
    )
    colour_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ColourName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    colour_system: Optional[str] = field(
        default=None,
        metadata={
            "name": "ColourSystem",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    back_ground_colour: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "BackGroundColour",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_length": 6,
            "format": "base16",
        }
    )
    background_colour_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "BackgroundColourName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    text_colour: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "TextColour",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_length": 6,
            "format": "base16",
        }
    )
    text_colour_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "TextColourName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    text_font: Optional[str] = field(
        default=None,
        metadata={
            "name": "TextFont",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    text_font_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "TextFontName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    text_language: Optional[str] = field(
        default=None,
        metadata={
            "name": "TextLanguage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    info_links: Optional[InfoLinksRelStructure] = field(
        default=None,
        metadata={
            "name": "infoLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
