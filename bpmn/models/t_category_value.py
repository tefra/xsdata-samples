from __future__ import annotations

from dataclasses import dataclass, field

from .t_base_element import TBaseElement

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TCategoryValue(TBaseElement):
    class Meta:
        name = "tCategoryValue"

    value: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
