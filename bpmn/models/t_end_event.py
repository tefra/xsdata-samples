from dataclasses import dataclass
from .t_throw_event import TThrowEvent

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TEndEvent(TThrowEvent):
    class Meta:
        name = "tEndEvent"
