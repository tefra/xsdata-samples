from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "urn:vpro:media:2009"


class ColorType(StrEnum):
    COLOR = "COLOR"
    BLACK_AND_WHITE = "BLACK AND WHITE"
    BLACK_AND_WHITE_AND_COLOR = "BLACK AND WHITE AND COLOR"
    COLORIZED = "COLORIZED"
