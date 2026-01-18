from __future__ import annotations

from dataclasses import dataclass

from .t_boundary_event import TBoundaryEvent

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class BoundaryEvent(TBoundaryEvent):
    class Meta:
        name = "boundaryEvent"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
