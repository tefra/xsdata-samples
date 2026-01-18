from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.w3.org/1998/Math/MathML"


class MathLinebreakstyle(Enum):
    BEFORE = "before"
    AFTER = "after"
    DUPLICATE = "duplicate"
    INFIXLINEBREAKSTYLE = "infixlinebreakstyle"
