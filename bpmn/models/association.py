from __future__ import annotations

from dataclasses import dataclass

from .t_association import TAssociation

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class Association(TAssociation):
    class Meta:
        name = "association"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
