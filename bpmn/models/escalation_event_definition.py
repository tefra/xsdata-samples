from __future__ import annotations

from dataclasses import dataclass

from .t_escalation_event_definition import TEscalationEventDefinition

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class EscalationEventDefinition(TEscalationEventDefinition):
    class Meta:
        name = "escalationEventDefinition"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
