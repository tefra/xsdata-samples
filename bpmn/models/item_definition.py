from __future__ import annotations

from dataclasses import dataclass

from .t_item_definition import TItemDefinition

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class ItemDefinition(TItemDefinition):
    class Meta:
        name = "itemDefinition"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
