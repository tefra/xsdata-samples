from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.air_price_point_list import AirPricePointList
from travelport.models.air_pricing_solution import AirPricingSolution
from travelport.models.alternate_location_distance_list import AlternateLocationDistanceList
from travelport.models.alternate_route_list import AlternateRouteList
from travelport.models.base_availability_search_rsp import BaseAvailabilitySearchRsp
from travelport.models.expert_solution_list import ExpertSolutionList
from travelport.models.fare_info_message import FareInfoMessage
from travelport.models.fare_note_list import FareNoteList
from travelport.models.rail_fare_idlist import RailFareIdlist
from travelport.models.rail_fare_list import RailFareList
from travelport.models.rail_fare_note_list import RailFareNoteList
from travelport.models.rail_journey_list import RailJourneyList
from travelport.models.rail_pricing_solution import RailPricingSolution
from travelport.models.rail_segment_list import RailSegmentList
from travelport.models.route_list import RouteList

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirSearchRsp(BaseAvailabilitySearchRsp):
    """
    Base Response for Air Search.
    """
    fare_note_list: None | FareNoteList = field(
        default=None,
        metadata={
            "name": "FareNoteList",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )
    expert_solution_list: None | ExpertSolutionList = field(
        default=None,
        metadata={
            "name": "ExpertSolutionList",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )
    route_list: None | RouteList = field(
        default=None,
        metadata={
            "name": "RouteList",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )
    alternate_route_list: None | AlternateRouteList = field(
        default=None,
        metadata={
            "name": "AlternateRouteList",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )
    alternate_location_distance_list: None | AlternateLocationDistanceList = field(
        default=None,
        metadata={
            "name": "AlternateLocationDistanceList",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )
    fare_info_message: list[FareInfoMessage] = field(
        default_factory=list,
        metadata={
            "name": "FareInfoMessage",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 99,
        }
    )
    air_pricing_solution: list[AirPricingSolution] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingSolution",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 999,
        }
    )
    air_price_point_list: None | AirPricePointList = field(
        default=None,
        metadata={
            "name": "AirPricePointList",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )
    rail_segment_list: None | RailSegmentList = field(
        default=None,
        metadata={
            "name": "RailSegmentList",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/rail_v52_0",
        }
    )
    rail_journey_list: None | RailJourneyList = field(
        default=None,
        metadata={
            "name": "RailJourneyList",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/rail_v52_0",
        }
    )
    rail_fare_note_list: None | RailFareNoteList = field(
        default=None,
        metadata={
            "name": "RailFareNoteList",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/rail_v52_0",
        }
    )
    rail_fare_idlist: None | RailFareIdlist = field(
        default=None,
        metadata={
            "name": "RailFareIDList",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/rail_v52_0",
        }
    )
    rail_fare_list: None | RailFareList = field(
        default=None,
        metadata={
            "name": "RailFareList",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/rail_v52_0",
        }
    )
    rail_pricing_solution: list[RailPricingSolution] = field(
        default_factory=list,
        metadata={
            "name": "RailPricingSolution",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/rail_v52_0",
            "max_occurs": 999,
        }
    )
