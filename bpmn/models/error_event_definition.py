from dataclasses import dataclass
from .t_error_event_definition import TErrorEventDefinition

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class ErrorEventDefinition(TErrorEventDefinition):
    class Meta:
        name = "errorEventDefinition"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
