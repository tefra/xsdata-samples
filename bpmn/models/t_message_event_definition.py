from __future__ import annotations

from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

from .t_event_definition import TEventDefinition

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class TMessageEventDefinition(TEventDefinition):
    class Meta:
        name = "tMessageEventDefinition"

    operation_ref: None | QName = field(
        default=None,
        metadata={
            "name": "operationRef",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    message_ref: None | QName = field(
        default=None,
        metadata={
            "name": "messageRef",
            "type": "Attribute",
        },
    )
