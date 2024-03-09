from __future__ import annotations

from dataclasses import dataclass

from npo.models.schedule_type import ScheduleType

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class Schedule(ScheduleType):
    """Programs of type 'BROADCAST' can contain schedule events.

    A schedule indicates on which channel and at what time the program
    is broadcast. A schedule is a container which contains the schedule
    events of different programs, for a certain period of time.
    """

    class Meta:
        name = "schedule"
        namespace = "urn:vpro:media:2009"
