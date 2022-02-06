from dataclasses import dataclass
from .t_catch_event import TCatchEvent

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TIntermediateCatchEvent(TCatchEvent):
    class Meta:
        name = "tIntermediateCatchEvent"
