from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


class TableFrame(StrEnum):
    ABOVE = "above"
    BELOW = "below"
    BORDER = "border"
    BOX = "box"
    HSIDES = "hsides"
    LHS = "lhs"
    RHS = "rhs"
    VOID = "void"
    VSIDES = "vsides"
