from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName
from .t_event_definition import TEventDefinition

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TCompensateEventDefinition(TEventDefinition):
    class Meta:
        name = "tCompensateEventDefinition"

    wait_for_completion: Optional[bool] = field(
        default=None,
        metadata={
            "name": "waitForCompletion",
            "type": "Attribute",
        },
    )
    activity_ref: Optional[QName] = field(
        default=None,
        metadata={
            "name": "activityRef",
            "type": "Attribute",
        },
    )
