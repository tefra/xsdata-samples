from __future__ import annotations

from dataclasses import dataclass

from .t_assignment import TAssignment

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class Assignment(TAssignment):
    class Meta:
        name = "assignment"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
