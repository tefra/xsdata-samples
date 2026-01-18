from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

from .t_event_definition import TEventDefinition

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TErrorEventDefinition(TEventDefinition):
    class Meta:
        name = "tErrorEventDefinition"

    error_ref: QName | None = field(
        default=None,
        metadata={
            "name": "errorRef",
            "type": "Attribute",
        },
    )
