from dataclasses import dataclass
from .t_resource_parameter import TResourceParameter

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class ResourceParameter(TResourceParameter):
    class Meta:
        name = "resourceParameter"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
