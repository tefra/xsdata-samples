from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_segment import AirSegment
from travelport.models.air_segment_special_update_action import (
    AirSegmentSpecialUpdateAction,
)

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class AirSegmentSpecialUpdate:
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    air_segment: None | AirSegment = field(
        default=None,
        metadata={
            "name": "AirSegment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "required": True,
        },
    )
    action: None | AirSegmentSpecialUpdateAction = field(
        default=None,
        metadata={
            "name": "Action",
            "type": "Attribute",
            "required": True,
        },
    )
