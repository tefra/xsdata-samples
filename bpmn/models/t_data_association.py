from __future__ import annotations

from dataclasses import dataclass, field

from .assignment import Assignment
from .t_base_element import TBaseElement
from .t_formal_expression import TFormalExpression

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class TDataAssociation(TBaseElement):
    class Meta:
        name = "tDataAssociation"

    source_ref: list[str] = field(
        default_factory=list,
        metadata={
            "name": "sourceRef",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    target_ref: str = field(
        metadata={
            "name": "targetRef",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
            "required": True,
        }
    )
    transformation: None | TFormalExpression = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    assignment: list[Assignment] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
