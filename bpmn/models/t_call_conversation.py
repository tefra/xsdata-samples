from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName

from .participant_association import ParticipantAssociation
from .t_conversation_node import TConversationNode

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TCallConversation(TConversationNode):
    class Meta:
        name = "tCallConversation"

    participant_association: list[ParticipantAssociation] = field(
        default_factory=list,
        metadata={
            "name": "participantAssociation",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    called_collaboration_ref: QName | None = field(
        default=None,
        metadata={
            "name": "calledCollaborationRef",
            "type": "Attribute",
        },
    )
