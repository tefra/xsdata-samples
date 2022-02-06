from dataclasses import dataclass
from .t_signal_event_definition import TSignalEventDefinition

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class SignalEventDefinition(TSignalEventDefinition):
    class Meta:
        name = "signalEventDefinition"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
