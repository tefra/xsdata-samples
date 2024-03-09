from dataclasses import dataclass, field
from typing import List, Optional
from xml.etree.ElementTree import QName

from .documentation import Documentation

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TExtension:
    class Meta:
        name = "tExtension"

    documentation: List[Documentation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    definition: Optional[QName] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    must_understand: bool = field(
        default=False,
        metadata={
            "name": "mustUnderstand",
            "type": "Attribute",
        },
    )
