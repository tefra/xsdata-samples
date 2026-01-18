from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

from .t_root_element import TRootElement

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TMessage(TRootElement):
    class Meta:
        name = "tMessage"

    name: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    item_ref: QName | None = field(
        default=None,
        metadata={
            "name": "itemRef",
            "type": "Attribute",
        },
    )
