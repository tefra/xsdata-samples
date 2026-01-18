from __future__ import annotations

from dataclasses import dataclass

from .t_implicit_throw_event import TImplicitThrowEvent

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class ImplicitThrowEvent(TImplicitThrowEvent):
    class Meta:
        name = "implicitThrowEvent"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
