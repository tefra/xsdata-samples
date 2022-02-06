from dataclasses import dataclass, field
from typing import List, Optional
from .assignment import Assignment
from .t_base_element import TBaseElement
from .t_formal_expression import TFormalExpression

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TDataAssociation(TBaseElement):
    class Meta:
        name = "tDataAssociation"

    source_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "sourceRef",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        }
    )
    target_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "targetRef",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
            "required": True,
        }
    )
    transformation: Optional[TFormalExpression] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        }
    )
    assignment: List[Assignment] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        }
    )
