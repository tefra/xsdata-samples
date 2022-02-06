from dataclasses import dataclass
from .t_exclusive_gateway import TExclusiveGateway

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class ExclusiveGateway(TExclusiveGateway):
    class Meta:
        name = "exclusiveGateway"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
