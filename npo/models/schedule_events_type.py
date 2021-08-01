from dataclasses import dataclass, field
from typing import List
from npo.models.schedule_event_type import ScheduleEventType

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class ScheduleEventsType:
    class Meta:
        name = "scheduleEventsType"

    schedule_event: List[ScheduleEventType] = field(
        default_factory=list,
        metadata={
            "name": "scheduleEvent",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
