from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.air_segment import AirSegment

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirSegmentError:
    """
    Container to return error messages corresponding to AirSegment.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_segment: None | AirSegment = field(
        default=None,
        metadata={
            "name": "AirSegment",
            "type": "Element",
            "required": True,
        }
    )
    error_message: None | str = field(
        default=None,
        metadata={
            "name": "ErrorMessage",
            "type": "Element",
            "required": True,
        }
    )
