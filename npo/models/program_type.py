from dataclasses import dataclass, field
from typing import List, Optional
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

    schedule_events: Optional[ScheduleEventsType] = field(
        default=None,
        metadata={
            "name": "scheduleEvents",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    episode_of: List[MemberRefType] = field(
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
    segments: Optional[SegmentsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    type: Optional[ProgramTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "doc": "The type of this program (e.g. BROADCAST, TRACK, CLIP)",
        }
    )
