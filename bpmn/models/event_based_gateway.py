from dataclasses import dataclass
from .t_event_based_gateway import TEventBasedGateway

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class EventBasedGateway(TEventBasedGateway):
    class Meta:
        name = "eventBasedGateway"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
