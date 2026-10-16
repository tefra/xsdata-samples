from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.w3.org/1999/xlink"


class ShowType(StrEnum):
    NEW = "new"
    REPLACE = "replace"
    EMBED = "embed"
    OTHER = "other"
    NONE = "none"
