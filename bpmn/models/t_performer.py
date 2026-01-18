from __future__ import annotations

from dataclasses import dataclass

from .t_resource_role import TResourceRole

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class TPerformer(TResourceRole):
    class Meta:
        name = "tPerformer"
