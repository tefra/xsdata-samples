from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlDuration

from npo.models.av_attributes_type import AvAttributesType
from npo.models.channel_enum import ChannelEnum
from npo.models.repeat_type import RepeatType
from npo.models.schedule_event_description import ScheduleEventDescription
from npo.models.schedule_event_title import ScheduleEventTitle
from npo.models.schedule_event_type_enum import ScheduleEventTypeEnum

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass(kw_only=True)
class ScheduleEventType:
    class Meta:
        name = "scheduleEventType"

    title: list[ScheduleEventTitle] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        },
    )
    description: list[ScheduleEventDescription] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        },
    )
    repeat: None | RepeatType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        },
    )
    member_of: None | str = field(
        default=None,
        metadata={
            "name": "memberOf",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        },
    )
    av_attributes: None | AvAttributesType = field(
        default=None,
        metadata={
            "name": "avAttributes",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        },
    )
    text_subtitles: None | str = field(
        default=None,
        metadata={
            "name": "textSubtitles",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        },
    )
    text_page: None | str = field(
        default=None,
        metadata={
            "name": "textPage",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        },
    )
    guide_day: XmlDate = field(
        metadata={
            "name": "guideDay",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "required": True,
        }
    )
    start: XmlDateTime = field(
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "required": True,
        }
    )
    offset: None | XmlDuration = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        },
    )
    duration: XmlDuration = field(
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "required": True,
        }
    )
    po_prog_id: None | str = field(
        default=None,
        metadata={
            "name": "poProgID",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        },
    )
    primary_lifestyle: None | str = field(
        default=None,
        metadata={
            "name": "primaryLifestyle",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        },
    )
    secondary_lifestyle: None | str = field(
        default=None,
        metadata={
            "name": "secondaryLifestyle",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        },
    )
    imi: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
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
    guide_day_attribute: None | XmlDate = field(
        default=None,
        metadata={
            "name": "guideDay",
            "type": "Attribute",
        },
    )
    mid_ref: str = field(
        metadata={
            "name": "midRef",
            "type": "Attribute",
            "required": True,
            "min_length": 4,
            "max_length": 255,
            "pattern": r"[ \.a-zA-Z0-9_-]+",
        }
    )
    urn_ref: str = field(
        metadata={
            "name": "urnRef",
            "type": "Attribute",
            "required": True,
        }
    )
    type_value: None | ScheduleEventTypeEnum = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
