from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


class TItemKind(StrEnum):
    INFORMATION = "Information"
    PHYSICAL = "Physical"
