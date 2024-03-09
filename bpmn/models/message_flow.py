from dataclasses import dataclass

from .t_message_flow import TMessageFlow

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class MessageFlow(TMessageFlow):
    class Meta:
        name = "messageFlow"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
