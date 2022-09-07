from enum import Enum

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


class TableRules(Enum):
    ALL = "all"
    COLS = "cols"
    GROUPS = "groups"
    NONE = "none"
    ROWS = "rows"
