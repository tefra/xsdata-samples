from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName

from .t_event_definition import TEventDefinition

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TSignalEventDefinition(TEventDefinition):
    class Meta:
        name = "tSignalEventDefinition"

    signal_ref: Optional[QName] = field(
        default=None,
        metadata={
            "name": "signalRef",
            "type": "Attribute",
        },
    )
