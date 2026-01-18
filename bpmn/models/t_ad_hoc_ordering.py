from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


class TAdHocOrdering(Enum):
    PARALLEL = "Parallel"
    SEQUENTIAL = "Sequential"
