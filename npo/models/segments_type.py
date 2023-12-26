from __future__ import annotations
from dataclasses import dataclass, field
from npo.models.segment_type import SegmentType

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class SegmentsType:
    class Meta:
        name = "segmentsType"

    segment: list[SegmentType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        },
    )
