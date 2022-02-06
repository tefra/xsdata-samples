from dataclasses import dataclass
from .t_escalation_event_definition import TEscalationEventDefinition

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class EscalationEventDefinition(TEscalationEventDefinition):
    class Meta:
        name = "escalationEventDefinition"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
