from dataclasses import dataclass

from .t_message_event_definition import TMessageEventDefinition

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class MessageEventDefinition(TMessageEventDefinition):
    class Meta:
        name = "messageEventDefinition"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
