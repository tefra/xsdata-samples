from dataclasses import dataclass

from .t_conversation_association import TConversationAssociation

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class ConversationAssociation(TConversationAssociation):
    class Meta:
        name = "conversationAssociation"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
