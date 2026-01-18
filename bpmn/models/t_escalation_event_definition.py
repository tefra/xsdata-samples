from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName

from .t_event_definition import TEventDefinition

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TEscalationEventDefinition(TEventDefinition):
    class Meta:
        name = "tEscalationEventDefinition"

    escalation_ref: QName | None = field(
        default=None,
        metadata={
            "name": "escalationRef",
            "type": "Attribute",
        },
    )
