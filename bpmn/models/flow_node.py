from __future__ import annotations

from dataclasses import dataclass

from .t_flow_node import TFlowNode

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class FlowNode(TFlowNode):
    class Meta:
        name = "flowNode"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
