from enum import Enum

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


class StringNameNameStyle(Enum):
    EASTERN = "eastern"
    GIVEN_ONLY = "given-only"
    ISLENSK = "islensk"
    WESTERN = "western"
