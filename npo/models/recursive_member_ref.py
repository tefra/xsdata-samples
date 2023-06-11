from __future__ import annotations
from dataclasses import dataclass, field
from npo.models.media_type_enum import MediaTypeEnum

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class RecursiveMemberRef:
    class Meta:
        name = "recursiveMemberRef"

    member_of: list[RecursiveMemberRef] = field(
        default_factory=list,
        metadata={
            "name": "memberOf",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    episode_of: list[RecursiveMemberRef] = field(
        default_factory=list,
        metadata={
            "name": "episodeOf",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    segment_of: None | RecursiveMemberRef = field(
        default=None,
        metadata={
            "name": "segmentOf",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    mid_ref: None | str = field(
        default=None,
        metadata={
            "name": "midRef",
            "type": "Attribute",
        }
    )
    type_value: None | MediaTypeEnum = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        }
    )
    index: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    highlighted: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
