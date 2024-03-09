from dataclasses import dataclass, field
from typing import List
from xml.etree.ElementTree import QName

from .t_flow_element import TFlowElement

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TFlowNode(TFlowElement):
    class Meta:
        name = "tFlowNode"

    incoming: List[QName] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    outgoing: List[QName] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
