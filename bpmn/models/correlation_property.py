from __future__ import annotations

from dataclasses import dataclass

from .t_correlation_property import TCorrelationProperty

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class CorrelationProperty(TCorrelationProperty):
    class Meta:
        name = "correlationProperty"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
