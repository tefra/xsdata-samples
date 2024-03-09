from dataclasses import dataclass

from .t_correlation_property_binding import TCorrelationPropertyBinding

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class CorrelationPropertyBinding(TCorrelationPropertyBinding):
    class Meta:
        name = "correlationPropertyBinding"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
