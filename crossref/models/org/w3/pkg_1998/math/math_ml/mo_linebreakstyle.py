from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.w3.org/1998/Math/MathML"


class MoLinebreakstyle(Enum):
    BEFORE = "before"
    AFTER = "after"
    DUPLICATE = "duplicate"
    INFIXLINEBREAKSTYLE = "infixlinebreakstyle"
