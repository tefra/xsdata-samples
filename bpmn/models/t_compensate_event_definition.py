from __future__ import annotations

from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

from .t_event_definition import TEventDefinition

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TCompensateEventDefinition(TEventDefinition):
    class Meta:
        name = "tCompensateEventDefinition"

    wait_for_completion: bool | None = field(
        default=None,
        metadata={
            "name": "waitForCompletion",
            "type": "Attribute",
        },
    )
    activity_ref: QName | None = field(
        default=None,
        metadata={
            "name": "activityRef",
            "type": "Attribute",
        },
    )
