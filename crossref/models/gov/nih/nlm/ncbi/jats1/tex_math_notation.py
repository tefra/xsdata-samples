from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


class TexMathNotation(StrEnum):
    LA_TE_X = "LaTeX"
    TEX = "TEX"
    TE_X_1 = "TeX"
    TEX_2 = "tex"
