from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.w3.org/1998/Math/MathML"


class MathIndentalign(StrEnum):
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"
    AUTO = "auto"
    ID = "id"
