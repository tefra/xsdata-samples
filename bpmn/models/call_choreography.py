from dataclasses import dataclass
from .t_call_choreography import TCallChoreography

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class CallChoreography(TCallChoreography):
    class Meta:
        name = "callChoreography"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
