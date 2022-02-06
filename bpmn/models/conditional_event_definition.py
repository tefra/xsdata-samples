from dataclasses import dataclass
from .t_conditional_event_definition import TConditionalEventDefinition

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class ConditionalEventDefinition(TConditionalEventDefinition):
    class Meta:
        name = "conditionalEventDefinition"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
