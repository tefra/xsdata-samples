from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.w3.org/1999/xlink"


class ActuateType(StrEnum):
    ON_LOAD = "onLoad"
    ON_REQUEST = "onRequest"
    OTHER = "other"
    NONE = "none"
