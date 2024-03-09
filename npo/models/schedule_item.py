from __future__ import annotations

from dataclasses import dataclass

from npo.models.schedule_event_api_type import ScheduleEventApiType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class ScheduleItem(ScheduleEventApiType):
    class Meta:
        name = "scheduleItem"
        namespace = "urn:vpro:api:2013"
