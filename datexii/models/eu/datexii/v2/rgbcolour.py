from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.multilingual_string import MultilingualString

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass(kw_only=True)
class RGBColour:
    """
    An RGB colour described by values for red, green and blue (0..255) as
    well as an optional name.

    :ivar rgb_red_value: The red value of the RGB colour (0..255).
    :ivar rgb_green_value: The green value of the RGB colour (0..255).
    :ivar rgb_blue_value: The blue value of the RGB colour (0..255).
    :ivar colour_name: The name of the colour.
    :ivar rgb_colour_extension:
    """

    rgb_red_value: int = field(
        metadata={
            "name": "rgbRedValue",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    rgb_green_value: int = field(
        metadata={
            "name": "rgbGreenValue",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    rgb_blue_value: int = field(
        metadata={
            "name": "rgbBlueValue",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    colour_name: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "colourName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    rgb_colour_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "rgbColourExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
