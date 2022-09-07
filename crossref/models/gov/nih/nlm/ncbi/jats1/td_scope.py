from enum import Enum

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


class TdScope(Enum):
    COL = "col"
    COLGROUP = "colgroup"
    ROW = "row"
    ROWGROUP = "rowgroup"
