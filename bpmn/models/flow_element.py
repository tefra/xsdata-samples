from dataclasses import dataclass
from .t_flow_element import TFlowElement

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class FlowElement(TFlowElement):
    class Meta:
        name = "flowElement"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
