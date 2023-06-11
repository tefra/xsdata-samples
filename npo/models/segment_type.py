from __future__ import annotations
from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDuration
from npo.models.base_media_type import BaseMediaType
from npo.models.recursive_member_ref import RecursiveMemberRef
from npo.models.segment_type_enum import SegmentTypeEnum

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class SegmentType(BaseMediaType):
    class Meta:
        name = "segmentType"

    segment_of: None | RecursiveMemberRef = field(
        default=None,
        metadata={
            "name": "segmentOf",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    start: None | XmlDuration = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "required": True,
        }
    )
    mid_ref: None | str = field(
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
    urn_ref: None | str = field(
        default=None,
        metadata={
            "name": "urnRef",
            "type": "Attribute",
            "required": True,
        }
    )
    type_value: None | SegmentTypeEnum = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        }
    )
