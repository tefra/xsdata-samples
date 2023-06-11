from __future__ import annotations
from dataclasses import dataclass, field
from npo.models.location_type import LocationType
from npo.models.schedule_event_type import ScheduleEventType

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class LocationTableType:
    class Meta:
        name = "locationTableType"

    location: list[LocationType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    schedule_event: list[ScheduleEventType] = field(
        default_factory=list,
        metadata={
            "name": "scheduleEvent",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
