from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_search_modifiers import AirSearchModifiers
from travelport.models.base_core_search_req_1 import BaseCoreSearchReq1
from travelport.models.journey_data import JourneyData
from travelport.models.search_air_leg import SearchAirLeg
from travelport.models.search_specific_air_segment import (
    SearchSpecificAirSegment,
)
from travelport.models.split_ticketing_search import SplitTicketingSearch

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class BaseAirSearchReq(BaseCoreSearchReq1):
    """
    Base Request for Low fare air Search.
    """

    search_air_leg: list[SearchAirLeg] = field(
        default_factory=list,
        metadata={
            "name": "SearchAirLeg",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 9,
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
    split_ticketing_search: None | SplitTicketingSearch = field(
        default=None,
        metadata={
            "name": "SplitTicketingSearch",
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
