from __future__ import annotations

from dataclasses import dataclass

from .t_compensate_event_definition import TCompensateEventDefinition

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class CompensateEventDefinition(TCompensateEventDefinition):
    class Meta:
        name = "compensateEventDefinition"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
