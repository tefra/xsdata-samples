from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


class TableRules(StrEnum):
    ALL = "all"
    COLS = "cols"
    GROUPS = "groups"
    NONE = "none"
    ROWS = "rows"
