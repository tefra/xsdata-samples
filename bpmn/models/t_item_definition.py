from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName

from .t_item_kind import TItemKind
from .t_root_element import TRootElement

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TItemDefinition(TRootElement):
    class Meta:
        name = "tItemDefinition"

    structure_ref: QName | None = field(
        default=None,
        metadata={
            "name": "structureRef",
            "type": "Attribute",
        },
    )
    is_collection: bool = field(
        default=False,
        metadata={
            "name": "isCollection",
            "type": "Attribute",
        },
    )
    item_kind: TItemKind = field(
        default=TItemKind.INFORMATION,
        metadata={
            "name": "itemKind",
            "type": "Attribute",
        },
    )
