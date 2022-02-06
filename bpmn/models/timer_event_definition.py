from dataclasses import dataclass
from .t_timer_event_definition import TTimerEventDefinition

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TimerEventDefinition(TTimerEventDefinition):
    class Meta:
        name = "timerEventDefinition"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
