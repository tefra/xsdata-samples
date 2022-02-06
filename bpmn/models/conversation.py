from dataclasses import dataclass
from .t_conversation import TConversation

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class Conversation(TConversation):
    class Meta:
        name = "conversation"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
