from __future__ import annotations

from dataclasses import dataclass

from .t_terminate_event_definition import TTerminateEventDefinition

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TerminateEventDefinition(TTerminateEventDefinition):
    class Meta:
        name = "terminateEventDefinition"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
