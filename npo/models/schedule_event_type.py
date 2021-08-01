from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDate, XmlDateTime, XmlDuration
from npo.models.av_attributes_type import AvAttributesType
from npo.models.channel_enum import ChannelEnum
from npo.models.repeat_type import RepeatType
from npo.models.schedule_event_description import ScheduleEventDescription
from npo.models.schedule_event_title import ScheduleEventTitle
from npo.models.schedule_event_type_enum import ScheduleEventTypeEnum

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class ScheduleEventType:
    class Meta:
        name = "scheduleEventType"

    title: List[ScheduleEventTitle] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    description: List[ScheduleEventDescription] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    repeat: Optional[RepeatType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    member_of: Optional[str] = field(
        default=None,
        metadata={
            "name": "memberOf",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    av_attributes: Optional[AvAttributesType] = field(
        default=None,
        metadata={
            "name": "avAttributes",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    text_subtitles: Optional[str] = field(
        default=None,
        metadata={
            "name": "textSubtitles",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    text_page: Optional[str] = field(
        default=None,
        metadata={
            "name": "textPage",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    guide_day: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "guideDay",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "required": True,
        }
    )
    start: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "required": True,
        }
    )
    offset: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "required": True,
        }
    )
    po_prog_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "poProgID",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    primary_lifestyle: Optional[str] = field(
        default=None,
        metadata={
            "name": "primaryLifestyle",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    secondary_lifestyle: Optional[str] = field(
        default=None,
        metadata={
            "name": "secondaryLifestyle",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    imi: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    channel: Optional[ChannelEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    net: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    guide_day_attribute: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "guideDay",
            "type": "Attribute",
        }
    )
    mid_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "midRef",
            "type": "Attribute",
            "required": True,
            "min_length": 4,
            "max_length": 255,
            "pattern": r"[ \.a-zA-Z0-9_-]+",
        }
    )
    urn_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "urnRef",
            "type": "Attribute",
            "required": True,
        }
    )
    type: Optional[ScheduleEventTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
