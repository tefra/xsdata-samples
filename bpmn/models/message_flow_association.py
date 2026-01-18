from __future__ import annotations

from dataclasses import dataclass

from .t_message_flow_association import TMessageFlowAssociation

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class MessageFlowAssociation(TMessageFlowAssociation):
    class Meta:
        name = "messageFlowAssociation"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
