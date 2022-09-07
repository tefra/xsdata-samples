from enum import Enum

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


class ThAlign(Enum):
    CENTER = "center"
    CHAR = "char"
    JUSTIFY = "justify"
    LEFT = "left"
    RIGHT = "right"
