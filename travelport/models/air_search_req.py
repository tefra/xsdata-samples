from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.air_search_modifiers import AirSearchModifiers
from travelport.models.base_search_req_1 import BaseSearchReq1
from travelport.models.journey_data import JourneyData
from travelport.models.point_of_commencement_1 import PointOfCommencement1
from travelport.models.search_air_leg import SearchAirLeg
from travelport.models.search_specific_air_segment import (
    SearchSpecificAirSegment,
)

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirSearchReq(BaseSearchReq1):
    """
    Base Request for Air Search.
    """

    point_of_commencement: None | PointOfCommencement1 = field(
        default=None,
        metadata={
            "name": "PointOfCommencement",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    search_air_leg: list[SearchAirLeg] = field(
        default_factory=list,
        metadata={
            "name": "SearchAirLeg",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 16,
        },
    )
    search_specific_air_segment: list[SearchSpecificAirSegment] = field(
        default_factory=list,
        metadata={
            "name": "SearchSpecificAirSegment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 999,
        },
    )
    air_search_modifiers: None | AirSearchModifiers = field(
        default=None,
        metadata={
            "name": "AirSearchModifiers",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        },
    )
    journey_data: None | JourneyData = field(
        default=None,
        metadata={
            "name": "JourneyData",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        },
    )
