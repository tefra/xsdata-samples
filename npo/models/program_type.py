from __future__ import annotations
from dataclasses import dataclass, field
from npo.models.base_media_type import BaseMediaType
from npo.models.member_ref_type import MemberRefType
from npo.models.program_type_enum import ProgramTypeEnum
from npo.models.schedule_events_type import ScheduleEventsType
from npo.models.segments_type import SegmentsType

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class ProgramType(BaseMediaType):
    class Meta:
        name = "programType"

    schedule_events: None | ScheduleEventsType = field(
        default=None,
        metadata={
            "name": "scheduleEvents",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    episode_of: list[MemberRefType] = field(
        default_factory=list,
        metadata={
            "name": "episodeOf",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "doc": (
                "A program (only if its type is 'BROADCAST') can be an episode"
                " of a group of type 'SERIES' or 'SEASON'."
            ),
        }
    )
    segments: None | SegmentsType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    type_value: None | ProgramTypeEnum = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
            "doc": "The type of this program (e.g. BROADCAST, TRACK, CLIP)",
        }
    )
