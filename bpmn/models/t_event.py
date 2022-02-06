from dataclasses import dataclass, field
from typing import List
from .property import Property
from .t_flow_node import TFlowNode

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TEvent(TFlowNode):
    class Meta:
        name = "tEvent"

    property: List[Property] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        }
    )
