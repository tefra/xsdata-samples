from dataclasses import dataclass
from .t_global_conversation import TGlobalConversation

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class GlobalConversation(TGlobalConversation):
    class Meta:
        name = "globalConversation"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
