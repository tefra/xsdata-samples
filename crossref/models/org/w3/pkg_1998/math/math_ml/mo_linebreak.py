from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.w3.org/1998/Math/MathML"


class MoLinebreak(StrEnum):
    AUTO = "auto"
    NEWLINE = "newline"
    NOBREAK = "nobreak"
    GOODBREAK = "goodbreak"
    BADBREAK = "badbreak"
