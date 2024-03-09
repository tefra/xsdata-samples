from dataclasses import dataclass

from .t_conversation_node import TConversationNode

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class ConversationNode(TConversationNode):
    class Meta:
        name = "conversationNode"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
