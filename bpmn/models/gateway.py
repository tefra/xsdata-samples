from dataclasses import dataclass
from .t_gateway import TGateway

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class Gateway(TGateway):
    class Meta:
        name = "gateway"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
