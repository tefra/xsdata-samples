from __future__ import annotations

from dataclasses import dataclass

from .t_escalation import TEscalation

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class Escalation(TEscalation):
    class Meta:
        name = "escalation"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
