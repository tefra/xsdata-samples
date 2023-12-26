from __future__ import annotations
from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDate, XmlDateTime
from npo.models.channel_enum import ChannelEnum
from npo.models.range_matcher_type import RangeMatcherType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class ScheduleEventSearchType(RangeMatcherType):
    class Meta:
        name = "scheduleEventSearchType"

    begin: None | XmlDateTime = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    end: None | XmlDateTime = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    channel: None | ChannelEnum = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    net: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
    rerun: None | bool = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        },
    )
