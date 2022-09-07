from enum import Enum

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


class TableFrame(Enum):
    ABOVE = "above"
    BELOW = "below"
    BORDER = "border"
    BOX = "box"
    HSIDES = "hsides"
    LHS = "lhs"
    RHS = "rhs"
    VOID = "void"
    VSIDES = "vsides"
