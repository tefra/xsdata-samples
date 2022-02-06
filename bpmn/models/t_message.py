from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName
from .t_root_element import TRootElement

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TMessage(TRootElement):
    class Meta:
        name = "tMessage"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    item_ref: Optional[QName] = field(
        default=None,
        metadata={
            "name": "itemRef",
            "type": "Attribute",
        }
    )
