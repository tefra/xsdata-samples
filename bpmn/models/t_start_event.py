from dataclasses import dataclass, field
from .t_catch_event import TCatchEvent

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TStartEvent(TCatchEvent):
    class Meta:
        name = "tStartEvent"

    is_interrupting: bool = field(
        default=True,
        metadata={
            "name": "isInterrupting",
            "type": "Attribute",
        },
    )
