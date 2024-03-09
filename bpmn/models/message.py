from dataclasses import dataclass

from .t_message import TMessage

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class Message(TMessage):
    class Meta:
        name = "message"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
