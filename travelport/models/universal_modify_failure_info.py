from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_segment_sell_failure_info import (
    AirSegmentSellFailureInfo,
)
from travelport.models.universal_modify_command_error import (
    UniversalModifyCommandError,
)

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class UniversalModifyFailureInfo:
    """
    Container to return air segment sell failures.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    universal_modify_command_error: list[UniversalModifyCommandError] = field(
        default_factory=list,
        metadata={
            "name": "UniversalModifyCommandError",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    air_segment_sell_failure_info: None | AirSegmentSellFailureInfo = field(
        default=None,
        metadata={
            "name": "AirSegmentSellFailureInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        },
    )
