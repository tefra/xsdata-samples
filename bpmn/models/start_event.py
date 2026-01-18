from __future__ import annotations

from dataclasses import dataclass

from .t_start_event import TStartEvent

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class StartEvent(TStartEvent):
    class Meta:
        name = "startEvent"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
