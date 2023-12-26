from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.air_segment_error import AirSegmentError
from travelport.models.type_error_info_1 import TypeErrorInfo1
from travelport.models.universal_modify_command_error import (
    UniversalModifyCommandError,
)

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class UniversalModifyErrorInfo(TypeErrorInfo1):
    """
    Container to return modify command errors.
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
    air_segment_error: list[AirSegmentError] = field(
        default_factory=list,
        metadata={
            "name": "AirSegmentError",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 999,
        },
    )
