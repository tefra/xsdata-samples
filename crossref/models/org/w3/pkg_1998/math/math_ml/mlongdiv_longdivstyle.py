from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.w3.org/1998/Math/MathML"


class MlongdivLongdivstyle(StrEnum):
    LEFTTOP = "lefttop"
    STACKEDRIGHTRIGHT = "stackedrightright"
    MEDIUMSTACKEDRIGHTRIGHT = "mediumstackedrightright"
    SHORTSTACKEDRIGHTRIGHT = "shortstackedrightright"
    RIGHTTOP = "righttop"
    LEFT_RIGHT = "left/\\right"
    LEFT_RIGHT_1 = "left)(right"
    RIGHT_RIGHT = ":right=right"
    STACKEDLEFTLEFT = "stackedleftleft"
    STACKEDLEFTLINETOP = "stackedleftlinetop"
