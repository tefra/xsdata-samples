from dataclasses import dataclass

from .t_event_definition import TEventDefinition

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TCancelEventDefinition(TEventDefinition):
    class Meta:
        name = "tCancelEventDefinition"
