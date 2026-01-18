from __future__ import annotations

from dataclasses import dataclass

from .t_potential_owner import TPotentialOwner

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class PotentialOwner(TPotentialOwner):
    class Meta:
        name = "potentialOwner"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
