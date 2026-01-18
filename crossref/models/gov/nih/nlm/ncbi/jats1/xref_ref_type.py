from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


class XrefRefType(Enum):
    AFF = "aff"
    APP = "app"
    AUTHOR_NOTES = "author-notes"
    AWARD = "award"
    BIBR = "bibr"
    BIO = "bio"
    BOXED_TEXT = "boxed-text"
    CHEM = "chem"
    COLLAB = "collab"
    CONTRIB = "contrib"
    CORRESP = "corresp"
    CUSTOM = "custom"
    DISP_FORMULA = "disp-formula"
    FIG = "fig"
    FN = "fn"
    KWD = "kwd"
    LIST = "list"
    OTHER = "other"
    PLATE = "plate"
    SCHEME = "scheme"
    SEC = "sec"
    STATEMENT = "statement"
    SUPPLEMENTARY_MATERIAL = "supplementary-material"
    TABLE = "table"
    TABLE_FN = "table-fn"
