from dataclasses import dataclass

from .t_cancel_event_definition import TCancelEventDefinition

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class CancelEventDefinition(TCancelEventDefinition):
    class Meta:
        name = "cancelEventDefinition"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
