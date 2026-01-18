from __future__ import annotations

from dataclasses import dataclass

from .t_group import TGroup

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class Group(TGroup):
    class Meta:
        name = "group"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
