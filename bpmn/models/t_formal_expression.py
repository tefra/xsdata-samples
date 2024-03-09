from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName

from .t_expression import TExpression

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TFormalExpression(TExpression):
    class Meta:
        name = "tFormalExpression"

    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    evaluates_to_type_ref: Optional[QName] = field(
        default=None,
        metadata={
            "name": "evaluatesToTypeRef",
            "type": "Attribute",
        },
    )
