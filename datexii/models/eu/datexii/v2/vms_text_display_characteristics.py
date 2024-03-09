from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.position_absolute_enum import (
    PositionAbsoluteEnum,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class VmsTextDisplayCharacteristics:
    """
    Characteristics specific to the textual display area on the VMS.

    :ivar text_lanterns_present: Indicates whether the VMS is equipped
        with flashing lanterns associated with the textual display area.
    :ivar text_page_sequencing_capable: Indicates whether the text
        display on the VMS is capable of sequencing through multiple
        pages of text. True = capable.
    :ivar text_pixels_across: Number of pixels horizontally across the
        textual display area of the VMS.
    :ivar text_pixels_down: Number of pixels vertically down the textual
        display area of the VMS.
    :ivar text_display_height: The vertical height measured in metres of
        the specific text display area.
    :ivar text_display_width: The horizontal width measured in metres of
        the specific text display area.
    :ivar max_number_of_characters: Maximum number of displayable
        characters on a single line in the textual display area of the
        VMS.
    :ivar max_number_of_rows: Maximum number of rows of displayable
        characters in the textual display area of the VMS.
    :ivar legend_code_list_identifier: Indicates which legend/text code
        list is referenced. This may be specific to the VMS type defined
        by vmsTypeCode.
    :ivar max_font_height: Maximum font height in pixels.
    :ivar min_font_height: Minimum font height in pixels.
    :ivar max_font_width: Maximum font width in pixels.
    :ivar min_font_width: Minimum font width in pixels.
    :ivar max_font_spacing: Maximum font spacing in pixels.
    :ivar min_font_spacing: Minimum font spacing in pixels.
    :ivar max_text_luminance_level: Maximum integer luminance level that
        is available on the textual display area of the VMS.
    :ivar max_number_of_sequential_pages: Maximum number of text pages
        which the VMS is capable of scrolling through sequentially, (2
        to n).
    :ivar text_position_absolute: The position of the area in which the
        text is displayed, e.g. at the left, right, top or bottom of the
        VMS display.
    :ivar text_position_x: The X-coordinate (horizontal) position of the
        area in which the text is displayed measured from the bottom
        left of the sign's overall display area to the bottom left of
        the specific text display area.
    :ivar text_position_y: The Y-coordinate (vertical) position of the
        area in which the text is displayed measured from the bottom
        left of the sign's overall display area to the bottom left of
        the specific text display area.
    :ivar vms_text_display_characteristics_extension:
    """

    text_lanterns_present: Optional[bool] = field(
        default=None,
        metadata={
            "name": "textLanternsPresent",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    text_page_sequencing_capable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "textPageSequencingCapable",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    text_pixels_across: Optional[int] = field(
        default=None,
        metadata={
            "name": "textPixelsAcross",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    text_pixels_down: Optional[int] = field(
        default=None,
        metadata={
            "name": "textPixelsDown",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    text_display_height: Optional[float] = field(
        default=None,
        metadata={
            "name": "textDisplayHeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    text_display_width: Optional[float] = field(
        default=None,
        metadata={
            "name": "textDisplayWidth",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    max_number_of_characters: Optional[int] = field(
        default=None,
        metadata={
            "name": "maxNumberOfCharacters",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    max_number_of_rows: Optional[int] = field(
        default=None,
        metadata={
            "name": "maxNumberOfRows",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    legend_code_list_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "legendCodeListIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        },
    )
    max_font_height: Optional[int] = field(
        default=None,
        metadata={
            "name": "maxFontHeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    min_font_height: Optional[int] = field(
        default=None,
        metadata={
            "name": "minFontHeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    max_font_width: Optional[int] = field(
        default=None,
        metadata={
            "name": "maxFontWidth",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    min_font_width: Optional[int] = field(
        default=None,
        metadata={
            "name": "minFontWidth",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    max_font_spacing: Optional[int] = field(
        default=None,
        metadata={
            "name": "maxFontSpacing",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    min_font_spacing: Optional[int] = field(
        default=None,
        metadata={
            "name": "minFontSpacing",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    max_text_luminance_level: Optional[int] = field(
        default=None,
        metadata={
            "name": "maxTextLuminanceLevel",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    max_number_of_sequential_pages: Optional[int] = field(
        default=None,
        metadata={
            "name": "maxNumberOfSequentialPages",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    text_position_absolute: Optional[PositionAbsoluteEnum] = field(
        default=None,
        metadata={
            "name": "textPositionAbsolute",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    text_position_x: Optional[float] = field(
        default=None,
        metadata={
            "name": "textPositionX",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    text_position_y: Optional[float] = field(
        default=None,
        metadata={
            "name": "textPositionY",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    vms_text_display_characteristics_extension: Optional[ExtensionType] = (
        field(
            default=None,
            metadata={
                "name": "vmsTextDisplayCharacteristicsExtension",
                "type": "Element",
                "namespace": "http://datex2.eu/schema/2/2_0",
            },
        )
    )
