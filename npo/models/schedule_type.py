from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate, XmlDateTime

from npo.models.channel_enum import ChannelEnum
from npo.models.schedule_event_type import ScheduleEventType

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass(kw_only=True)
class ScheduleType:
    class Meta:
        name = "scheduleType"

    schedule_event: list[ScheduleEventType] = field(
        default_factory=list,
        metadata={
            "name": "scheduleEvent",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "min_occurs": 1,
        },
    )
    channel: None | ChannelEnum = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    net: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    date: None | XmlDate = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    release_version: None | int = field(
        default=None,
        metadata={
            "name": "releaseVersion",
            "type": "Attribute",
        },
    )
    start: None | XmlDateTime = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    stop: None | XmlDateTime = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    reruns: None | bool = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
