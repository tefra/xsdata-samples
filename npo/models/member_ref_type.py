from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

from npo.models.media_type_enum import MediaTypeEnum
from npo.models.recursive_member_ref import RecursiveMemberRef

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass(kw_only=True)
class MemberRefType:
    class Meta:
        name = "memberRefType"

    episode_of: list[RecursiveMemberRef] = field(
        default_factory=list,
        metadata={
            "name": "episodeOf",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        },
    )
    member_of: list[RecursiveMemberRef] = field(
        default_factory=list,
        metadata={
            "name": "memberOf",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        },
    )
    segment_of: None | RecursiveMemberRef = field(
        default=None,
        metadata={
            "name": "segmentOf",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        },
    )
    mid_ref: None | str = field(
        default=None,
        metadata={
            "name": "midRef",
            "type": "Attribute",
            "min_length": 4,
            "max_length": 255,
            "pattern": r"[ \.a-zA-Z0-9_-]+",
            "doc": "Reference to the MID of the parent of this object.",
        },
    )
    urn_ref: None | str = field(
        default=None,
        metadata={
            "name": "urnRef",
            "type": "Attribute",
            "doc": (
                "Reference to the URN of the parent of this object. URN's are "
                "no longer actively used, but the attribute is\nstill "
                "available for backwards compatibility."
            ),
        },
    )
    crid_ref: None | str = field(
        default=None,
        metadata={
            "name": "cridRef",
            "type": "Attribute",
            "doc": (
                "Reference to a crid of the parent of this object. This is "
                "only used for imports from systems that cannot\nsupply a MID "
                "or URN. POMS does not export or publish parent crids."
            ),
        },
    )
    type_value: None | MediaTypeEnum = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
    index: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    highlighted: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    added: None | XmlDateTime = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
