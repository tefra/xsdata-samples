from enum import Enum

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


class TheadAlign(Enum):
    CENTER = "center"
    CHAR = "char"
    JUSTIFY = "justify"
    LEFT = "left"
    RIGHT = "right"
