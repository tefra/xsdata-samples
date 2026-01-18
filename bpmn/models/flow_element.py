from __future__ import annotations

from dataclasses import dataclass

from .t_flow_element import TFlowElement

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class FlowElement(TFlowElement):
    class Meta:
        name = "flowElement"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
