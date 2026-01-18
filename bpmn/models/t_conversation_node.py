from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName

from .correlation_key import CorrelationKey
from .t_base_element import TBaseElement

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TConversationNode(TBaseElement):
    class Meta:
        name = "tConversationNode"

    participant_ref: list[QName] = field(
        default_factory=list,
        metadata={
            "name": "participantRef",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    message_flow_ref: list[QName] = field(
        default_factory=list,
        metadata={
            "name": "messageFlowRef",
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
    name: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
