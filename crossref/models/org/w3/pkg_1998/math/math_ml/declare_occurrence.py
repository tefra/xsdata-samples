from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.w3.org/1998/Math/MathML"


class DeclareOccurrence(StrEnum):
    PREFIX = "prefix"
    INFIX = "infix"
    FUNCTION_MODEL = "function-model"
