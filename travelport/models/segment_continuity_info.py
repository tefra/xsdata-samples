from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.arvl_unkn_segment import ArvlUnknSegment
from travelport.models.continuity_override_remark import (
    ContinuityOverrideRemark,
)

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass(kw_only=True)
class SegmentContinuityInfo:
    """
    This container holds Arnks and segment continuity remarks.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    arvl_unkn_segment: list[ArvlUnknSegment] = field(
        default_factory=list,
        metadata={
            "name": "ArvlUnknSegment",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    continuity_override_remark: list[ContinuityOverrideRemark] = field(
        default_factory=list,
        metadata={
            "name": "ContinuityOverrideRemark",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    arrival_unknown_segment_count: None | int = field(
        default=None,
        metadata={
            "name": "ArrivalUnknownSegmentCount",
            "type": "Attribute",
        },
    )
