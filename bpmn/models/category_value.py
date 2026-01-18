from __future__ import annotations

from dataclasses import dataclass

from .t_category_value import TCategoryValue

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class CategoryValue(TCategoryValue):
    class Meta:
        name = "categoryValue"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
