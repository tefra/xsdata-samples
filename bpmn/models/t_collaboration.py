from __future__ import annotations

from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

from .artifact import Artifact
from .association import Association
from .call_conversation import CallConversation
from .conversation import Conversation
from .conversation_association import ConversationAssociation
from .conversation_link import ConversationLink
from .conversation_node import ConversationNode
from .correlation_key import CorrelationKey
from .group import Group
from .message_flow import MessageFlow
from .message_flow_association import MessageFlowAssociation
from .participant import Participant
from .participant_association import ParticipantAssociation
from .t_root_element import TRootElement
from .t_sub_conversation import SubConversation
from .text_annotation import TextAnnotation

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class TCollaboration(TRootElement):
    class Meta:
        name = "tCollaboration"

    participant: list[Participant] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    message_flow: list[MessageFlow] = field(
        default_factory=list,
        metadata={
            "name": "messageFlow",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    text_annotation: list[TextAnnotation] = field(
        default_factory=list,
        metadata={
            "name": "textAnnotation",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    group: list[Group] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    association: list[Association] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    artifact: list[Artifact] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
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
    conversation_association: list[ConversationAssociation] = field(
        default_factory=list,
        metadata={
            "name": "conversationAssociation",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    participant_association: list[ParticipantAssociation] = field(
        default_factory=list,
        metadata={
            "name": "participantAssociation",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    message_flow_association: list[MessageFlowAssociation] = field(
        default_factory=list,
        metadata={
            "name": "messageFlowAssociation",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    correlation_key: list[CorrelationKey] = field(
        default_factory=list,
        metadata={
            "name": "correlationKey",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    choreography_ref: list[QName] = field(
        default_factory=list,
        metadata={
            "name": "choreographyRef",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    conversation_link: list[ConversationLink] = field(
        default_factory=list,
        metadata={
            "name": "conversationLink",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    is_closed: bool = field(
        default=False,
        metadata={
            "name": "isClosed",
            "type": "Attribute",
        },
    )
