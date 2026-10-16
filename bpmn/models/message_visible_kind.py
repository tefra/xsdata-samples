from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/DI"


class MessageVisibleKind(StrEnum):
    INITIATING = "initiating"
    NON_INITIATING = "non_initiating"
