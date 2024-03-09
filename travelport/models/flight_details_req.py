from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_segment import AirSegment
from travelport.models.base_req_1 import BaseReq1

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class FlightDetailsReq(BaseReq1):
    """
    Request for the Flight Details of segments.

    Parameters
    ----------
    air_segment
        Provider: 1G,1V,1P.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_segment: list[AirSegment] = field(
        default_factory=list,
        metadata={
            "name": "AirSegment",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
