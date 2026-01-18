from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_segment import AirSegment

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class AirSegmentError:
    """
    Container to return error messages corresponding to AirSegment.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_segment: AirSegment = field(
        metadata={
            "name": "AirSegment",
            "type": "Element",
            "required": True,
        }
    )
    error_message: str = field(
        metadata={
            "name": "ErrorMessage",
            "type": "Element",
            "required": True,
        }
    )
