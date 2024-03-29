from dataclasses import dataclass

from .t_correlation_subscription import TCorrelationSubscription

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class CorrelationSubscription(TCorrelationSubscription):
    class Meta:
        name = "correlationSubscription"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
