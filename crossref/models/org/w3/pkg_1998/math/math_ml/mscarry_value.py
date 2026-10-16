from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.w3.org/1998/Math/MathML"


class MscarryValue(StrEnum):
    NONE = "none"
    UPDIAGONALSTRIKE = "updiagonalstrike"
    DOWNDIAGONALSTRIKE = "downdiagonalstrike"
    VERTICALSTRIKE = "verticalstrike"
    HORIZONTALSTRIKE = "horizontalstrike"
