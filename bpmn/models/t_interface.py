from dataclasses import dataclass, field
from typing import List, Optional
from xml.etree.ElementTree import QName

from .operation import Operation
from .t_root_element import TRootElement

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TInterface(TRootElement):
    class Meta:
        name = "tInterface"

    operation: List[Operation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
            "min_occurs": 1,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    implementation_ref: Optional[QName] = field(
        default=None,
        metadata={
            "name": "implementationRef",
            "type": "Attribute",
        },
    )
