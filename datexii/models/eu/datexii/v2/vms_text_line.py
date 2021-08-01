from dataclasses import dataclass, field
from typing import Optional
from datexii.models.eu.datexii.v2.colour_enum import ColourEnum
from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class VmsTextLine:
    """
    A single line of text on a text display area or supplementary panel.

    :ivar vms_text_line: A free-text string that is displayed on a
        single line on the text display area.
    :ivar vms_text_line_language: The language of the displayed line of
        text, specified by an ISO 639-2 3-alpha code.
    :ivar vms_text_line_colour: The colour of the displayed line of
        text.
    :ivar vms_text_line_flashing: Indication of whether the displayed
        line of text is flashing.
    :ivar vms_text_line_html: The displayed line of text defined by an
        HTML string showing text formatting tags.
    :ivar vms_text_line_extension:
    """
    vms_text_line: Optional[str] = field(
        default=None,
        metadata={
            "name": "vmsTextLine",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
            "max_length": 1024,
        }
    )
    vms_text_line_language: Optional[str] = field(
        default=None,
        metadata={
            "name": "vmsTextLineLanguage",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vms_text_line_colour: Optional[ColourEnum] = field(
        default=None,
        metadata={
            "name": "vmsTextLineColour",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vms_text_line_flashing: Optional[bool] = field(
        default=None,
        metadata={
            "name": "vmsTextLineFlashing",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vms_text_line_html: Optional[str] = field(
        default=None,
        metadata={
            "name": "vmsTextLineHtml",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        }
    )
    vms_text_line_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "vmsTextLineExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
