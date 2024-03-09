from dataclasses import dataclass

from .t_formal_expression import TFormalExpression

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class FormalExpression(TFormalExpression):
    class Meta:
        name = "formalExpression"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
