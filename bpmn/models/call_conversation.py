from __future__ import annotations

from dataclasses import dataclass

from .t_call_conversation import TCallConversation

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class CallConversation(TCallConversation):
    class Meta:
        name = "callConversation"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
