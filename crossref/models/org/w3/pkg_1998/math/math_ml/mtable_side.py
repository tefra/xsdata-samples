from enum import Enum

__NAMESPACE__ = "http://www.w3.org/1998/Math/MathML"


class MtableSide(Enum):
    LEFT = "left"
    RIGHT = "right"
    LEFTOVERLAP = "leftoverlap"
    RIGHTOVERLAP = "rightoverlap"
