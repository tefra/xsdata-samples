from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.w3.org/1998/Math/MathML"


class MathOverflow(Enum):
    LINEBREAK = "linebreak"
    SCROLL = "scroll"
    ELIDE = "elide"
    TRUNCATE = "truncate"
    SCALE = "scale"
