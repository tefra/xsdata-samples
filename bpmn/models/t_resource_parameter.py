from __future__ import annotations

from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

from .t_base_element import TBaseElement

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TResourceParameter(TBaseElement):
    class Meta:
        name = "tResourceParameter"

    name: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    type_value: QName | None = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
    is_required: bool | None = field(
        default=None,
        metadata={
            "name": "isRequired",
            "type": "Attribute",
        },
    )
