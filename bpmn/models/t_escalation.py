from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName

from .t_root_element import TRootElement

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TEscalation(TRootElement):
    class Meta:
        name = "tEscalation"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    escalation_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "escalationCode",
            "type": "Attribute",
        },
    )
    structure_ref: Optional[QName] = field(
        default=None,
        metadata={
            "name": "structureRef",
            "type": "Attribute",
        },
    )
