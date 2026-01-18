from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

from .t_expression import TExpression

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TFormalExpression(TExpression):
    class Meta:
        name = "tFormalExpression"

    language: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    evaluates_to_type_ref: QName | None = field(
        default=None,
        metadata={
            "name": "evaluatesToTypeRef",
            "type": "Attribute",
        },
    )
