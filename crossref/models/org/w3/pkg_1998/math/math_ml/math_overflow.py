from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.w3.org/1998/Math/MathML"


class MathOverflow(StrEnum):
    LINEBREAK = "linebreak"
    SCROLL = "scroll"
    ELIDE = "elide"
    TRUNCATE = "truncate"
    SCALE = "scale"
