from __future__ import annotations

from dataclasses import dataclass

from .t_message import TMessage

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class Message(TMessage):
    class Meta:
        name = "message"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
