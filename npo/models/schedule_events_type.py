from __future__ import annotations

from dataclasses import dataclass, field

from npo.models.schedule_event_type import ScheduleEventType

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass(kw_only=True)
class ScheduleEventsType:
    class Meta:
        name = "scheduleEventsType"

    schedule_event: list[ScheduleEventType] = field(
        default_factory=list,
        metadata={
            "name": "scheduleEvent",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        },
    )
