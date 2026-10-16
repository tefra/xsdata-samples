from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.w3.org/1998/Math/MathML"


class Linestyle(StrEnum):
    NONE = "none"
    SOLID = "solid"
    DASHED = "dashed"
