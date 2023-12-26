from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName
from .t_base_element import TBaseElement

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TResourceParameter(TBaseElement):
    class Meta:
        name = "tResourceParameter"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    type_value: Optional[QName] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
    is_required: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isRequired",
            "type": "Attribute",
        },
    )
