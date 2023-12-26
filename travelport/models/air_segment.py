from __future__ import annotations
from dataclasses import dataclass
from travelport.models.type_base_air_segment import TypeBaseAirSegment

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirSegment(TypeBaseAirSegment):
    """
    An Air marketable travel segment.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"
