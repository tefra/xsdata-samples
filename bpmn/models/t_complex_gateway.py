from dataclasses import dataclass, field
from typing import Optional
from .t_expression import TExpression
from .t_gateway import TGateway

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TComplexGateway(TGateway):
    class Meta:
        name = "tComplexGateway"

    activation_condition: Optional[TExpression] = field(
        default=None,
        metadata={
            "name": "activationCondition",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    default: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
