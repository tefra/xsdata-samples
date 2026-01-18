from __future__ import annotations

from dataclasses import dataclass

from .t_collaboration import TCollaboration

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TGlobalConversation(TCollaboration):
    class Meta:
        name = "tGlobalConversation"
