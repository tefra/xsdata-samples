from enum import Enum

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


class ColValign(Enum):
    BASELINE = "baseline"
    BOTTOM = "bottom"
    MIDDLE = "middle"
    TOP = "top"