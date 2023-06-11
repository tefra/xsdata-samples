from __future__ import annotations
from dataclasses import dataclass, field
from npo.models.group import Group
from npo.models.program import Program
from npo.models.schedule_event_type import ScheduleEventType
from npo.models.segment import Segment

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class ScheduleEventApiType(ScheduleEventType):
    class Meta:
        name = "scheduleEventApiType"

    program: None | Program = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    group: None | Group = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    segment: None | Segment = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
