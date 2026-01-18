from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.w3.org/1998/Math/MathML"


class DeclareOccurrence(Enum):
    PREFIX = "prefix"
    INFIX = "infix"
    FUNCTION_MODEL = "function-model"
