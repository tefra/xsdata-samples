from __future__ import annotations

from dataclasses import dataclass, field

from .t_expression import TExpression
from .t_flow_element import TFlowElement

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class TSequenceFlow(TFlowElement):
    class Meta:
        name = "tSequenceFlow"

    condition_expression: None | TExpression = field(
        default=None,
        metadata={
            "name": "conditionExpression",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    source_ref: str = field(
        metadata={
            "name": "sourceRef",
            "type": "Attribute",
            "required": True,
        }
    )
    target_ref: str = field(
        metadata={
            "name": "targetRef",
            "type": "Attribute",
            "required": True,
        }
    )
    is_immediate: None | bool = field(
        default=None,
        metadata={
            "name": "isImmediate",
            "type": "Attribute",
        },
    )
