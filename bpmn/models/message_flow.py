from __future__ import annotations

from dataclasses import dataclass

from .t_message_flow import TMessageFlow

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class MessageFlow(TMessageFlow):
    class Meta:
        name = "messageFlow"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
