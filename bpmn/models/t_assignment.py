from __future__ import annotations

from dataclasses import dataclass, field

from .t_base_element import TBaseElement
from .t_expression import TExpression

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class TAssignment(TBaseElement):
    class Meta:
        name = "tAssignment"

    from_value: TExpression = field(
        metadata={
            "name": "from",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
            "required": True,
        }
    )
    to: TExpression = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
            "required": True,
        }
    )
