from __future__ import annotations

from dataclasses import dataclass, field

from .t_expression import TExpression
from .t_gateway import TGateway

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TComplexGateway(TGateway):
    class Meta:
        name = "tComplexGateway"

    activation_condition: None | TExpression = field(
        default=None,
        metadata={
            "name": "activationCondition",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    default: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
