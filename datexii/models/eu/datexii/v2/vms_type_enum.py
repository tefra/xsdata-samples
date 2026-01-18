from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class VmsTypeEnum(Enum):
    """
    Type of variable message sign.

    :cvar COLOUR_GRAPHIC: A colour graphic display.
    :cvar CONTINUOUS_SIGN: A sign implementing fixed messages which are
        selected by electromechanical means.
    :cvar MONOCHROME_GRAPHIC: A monochrome graphic display.
    :cvar MATRIX_SIGN: Simple display made up of a fixed matrix of
        pixels (e.g. sets of LEDs or lights) capable of showing a
        limited set of aspects (or matrix images). The display area is
        regarded as a pictogram area in DATEX II.
    :cvar OTHER: Other than as defined in this enumeration.
    """

    COLOUR_GRAPHIC = "colourGraphic"
    CONTINUOUS_SIGN = "continuousSign"
    MONOCHROME_GRAPHIC = "monochromeGraphic"
    MATRIX_SIGN = "matrixSign"
    OTHER = "other"
