from __future__ import annotations

from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

from .t_expression import TExpression

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class TFormalExpression(TExpression):
    class Meta:
        name = "tFormalExpression"

    language: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    evaluates_to_type_ref: None | QName = field(
        default=None,
        metadata={
            "name": "evaluatesToTypeRef",
            "type": "Attribute",
        },
    )
