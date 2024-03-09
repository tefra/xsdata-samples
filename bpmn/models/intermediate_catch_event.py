from dataclasses import dataclass

from .t_intermediate_catch_event import TIntermediateCatchEvent

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class IntermediateCatchEvent(TIntermediateCatchEvent):
    class Meta:
        name = "intermediateCatchEvent"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
