from __future__ import annotations

from dataclasses import dataclass

from .t_correlation_key import TCorrelationKey

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class CorrelationKey(TCorrelationKey):
    class Meta:
        name = "correlationKey"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
