from dataclasses import dataclass
from .t_message_flow_association import TMessageFlowAssociation

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class MessageFlowAssociation(TMessageFlowAssociation):
    class Meta:
        name = "messageFlowAssociation"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
