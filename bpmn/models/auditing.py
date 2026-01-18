from __future__ import annotations

from dataclasses import dataclass

from .t_auditing import TAuditing

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class Auditing(TAuditing):
    class Meta:
        name = "auditing"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
