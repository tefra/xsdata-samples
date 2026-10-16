from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


class ThAlign(StrEnum):
    CENTER = "center"
    CHAR = "char"
    JUSTIFY = "justify"
    LEFT = "left"
    RIGHT = "right"
