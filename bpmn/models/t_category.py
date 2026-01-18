from __future__ import annotations

from dataclasses import dataclass, field

from .category_value import CategoryValue
from .t_root_element import TRootElement

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TCategory(TRootElement):
    class Meta:
        name = "tCategory"

    category_value: list[CategoryValue] = field(
        default_factory=list,
        metadata={
            "name": "categoryValue",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    name: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
