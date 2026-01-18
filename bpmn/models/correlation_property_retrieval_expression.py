from __future__ import annotations

from dataclasses import dataclass

from .t_correlation_property_retrieval_expression import (
    TCorrelationPropertyRetrievalExpression,
)

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class CorrelationPropertyRetrievalExpression(
    TCorrelationPropertyRetrievalExpression
):
    class Meta:
        name = "correlationPropertyRetrievalExpression"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
