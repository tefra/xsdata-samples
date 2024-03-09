from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName

from .t_catch_event import TCatchEvent

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TBoundaryEvent(TCatchEvent):
    class Meta:
        name = "tBoundaryEvent"

    cancel_activity: bool = field(
        default=True,
        metadata={
            "name": "cancelActivity",
            "type": "Attribute",
        },
    )
    attached_to_ref: Optional[QName] = field(
        default=None,
        metadata={
            "name": "attachedToRef",
            "type": "Attribute",
            "required": True,
        },
    )
