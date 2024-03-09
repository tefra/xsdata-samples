from dataclasses import dataclass, field
from typing import Optional

from .t_base_element import TBaseElement
from .t_expression import TExpression

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TAssignment(TBaseElement):
    class Meta:
        name = "tAssignment"

    from_value: Optional[TExpression] = field(
        default=None,
        metadata={
            "name": "from",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
            "required": True,
        },
    )
    to: Optional[TExpression] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
            "required": True,
        },
    )
