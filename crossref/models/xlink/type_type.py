from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.w3.org/1999/xlink"


class TypeType(StrEnum):
    SIMPLE = "simple"
    EXTENDED = "extended"
    TITLE = "title"
    RESOURCE = "resource"
    LOCATOR = "locator"
    ARC = "arc"
