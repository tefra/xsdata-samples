from __future__ import annotations

from dataclasses import dataclass, field

from .t_base_element import TBaseElement

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TDataState(TBaseElement):
    class Meta:
        name = "tDataState"

    name: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
