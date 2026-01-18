from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/DI"


class ParticipantBandKind(Enum):
    TOP_INITIATING = "top_initiating"
    MIDDLE_INITIATING = "middle_initiating"
    BOTTOM_INITIATING = "bottom_initiating"
    TOP_NON_INITIATING = "top_non_initiating"
    MIDDLE_NON_INITIATING = "middle_non_initiating"
    BOTTOM_NON_INITIATING = "bottom_non_initiating"
