from __future__ import annotations

from dataclasses import dataclass

from .t_event import TEvent

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class Event(TEvent):
    class Meta:
        name = "event"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
