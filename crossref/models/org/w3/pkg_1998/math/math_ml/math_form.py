from enum import Enum

__NAMESPACE__ = "http://www.w3.org/1998/Math/MathML"


class MathForm(Enum):
    PREFIX = "prefix"
    INFIX = "infix"
    POSTFIX = "postfix"
