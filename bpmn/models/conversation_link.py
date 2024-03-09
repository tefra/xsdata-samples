from dataclasses import dataclass

from .t_conversation_link import TConversationLink

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class ConversationLink(TConversationLink):
    class Meta:
        name = "conversationLink"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
