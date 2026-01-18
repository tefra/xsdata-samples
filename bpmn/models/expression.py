from __future__ import annotations

from dataclasses import dataclass

from .t_expression import TExpression

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class Expression(TExpression):
    class Meta:
        name = "expression"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
