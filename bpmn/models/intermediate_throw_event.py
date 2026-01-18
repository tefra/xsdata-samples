from __future__ import annotations

from dataclasses import dataclass

from .t_intermediate_throw_event import TIntermediateThrowEvent

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class IntermediateThrowEvent(TIntermediateThrowEvent):
    class Meta:
        name = "intermediateThrowEvent"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
