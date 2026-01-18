from __future__ import annotations

from dataclasses import dataclass

from .t_event_definition import TEventDefinition

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class EventDefinition(TEventDefinition):
    class Meta:
        name = "eventDefinition"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
