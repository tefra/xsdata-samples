from dataclasses import dataclass
from .t_correlation_key import TCorrelationKey

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class CorrelationKey(TCorrelationKey):
    class Meta:
        name = "correlationKey"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
