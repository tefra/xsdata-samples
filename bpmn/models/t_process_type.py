from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


class TProcessType(StrEnum):
    NONE = "None"
    PUBLIC = "Public"
    PRIVATE = "Private"
