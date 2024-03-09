from dataclasses import dataclass

from .t_resource_parameter_binding import TResourceParameterBinding

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class ResourceParameterBinding(TResourceParameterBinding):
    class Meta:
        name = "resourceParameterBinding"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
