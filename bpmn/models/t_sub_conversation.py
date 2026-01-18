from __future__ import annotations

from dataclasses import dataclass, field

from .call_conversation import CallConversation
from .conversation import Conversation
from .conversation_node import ConversationNode
from .t_conversation_node import TConversationNode

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TSubConversation(TConversationNode):
    class Meta:
        name = "tSubConversation"

    sub_conversation: list[SubConversation] = field(
        default_factory=list,
        metadata={
            "name": "subConversation",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    conversation: list[Conversation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    call_conversation: list[CallConversation] = field(
        default_factory=list,
        metadata={
            "name": "callConversation",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    conversation_node: list[ConversationNode] = field(
        default_factory=list,
        metadata={
            "name": "conversationNode",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )


@dataclass
class SubConversation(TSubConversation):
    class Meta:
        name = "subConversation"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
