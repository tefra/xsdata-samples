from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_req_1 import BaseReq1
from travelport.models.host_token_list_1 import HostTokenList1
from travelport.models.rail_fare_note_list import RailFareNoteList
from travelport.models.rail_pricing_solution import RailPricingSolution
from travelport.models.rail_search_modifiers import RailSearchModifiers
from travelport.models.search_passenger_1 import SearchPassenger1
from travelport.models.search_rail_leg import SearchRailLeg
from travelport.models.type_response_type import TypeResponseType

__NAMESPACE__ = "http://www.travelport.com/schema/rail_v52_0"


@dataclass
class RailExchangeQuoteReq(BaseReq1):
    """
    Queries the host for availability.

    Parameters
    ----------
    search_rail_leg
    rail_search_modifiers
    search_passenger
        Maxinumber of passenger increased in to 18 to support 9 INF
        passenger along with 9 ADT,CHD,INS
        passenger
    host_token_list
    rail_pricing_solution
    rail_fare_note_list
        List of RailFareNote(s) that is referenced by key in RailFare.
    locator_code
        The unique identifier for this rail reservation
    response_type
        Indicates the type of information to be returned in
        RailShopModifyAPIResponse.  Values are “Schedules” or “Availability”
        or “Fares”.  If not sent, “Fares” will be mapped if the request is
        for a specific rail segments, otherwise “Availability” will be
        mapped. Provider Supported RCH.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    search_rail_leg: list[SearchRailLeg] = field(
        default_factory=list,
        metadata={
            "name": "SearchRailLeg",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 9,
        }
    )
    rail_search_modifiers: None | RailSearchModifiers = field(
        default=None,
        metadata={
            "name": "RailSearchModifiers",
            "type": "Element",
        }
    )
    search_passenger: list[SearchPassenger1] = field(
        default_factory=list,
        metadata={
            "name": "SearchPassenger",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 18,
        }
    )
    host_token_list: None | HostTokenList1 = field(
        default=None,
        metadata={
            "name": "HostTokenList",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    rail_pricing_solution: None | RailPricingSolution = field(
        default=None,
        metadata={
            "name": "RailPricingSolution",
            "type": "Element",
        }
    )
    rail_fare_note_list: None | RailFareNoteList = field(
        default=None,
        metadata={
            "name": "RailFareNoteList",
            "type": "Element",
        }
    )
    locator_code: None | str = field(
        default=None,
        metadata={
            "name": "LocatorCode",
            "type": "Attribute",
            "required": True,
            "min_length": 5,
            "max_length": 8,
        }
    )
    response_type: None | TypeResponseType = field(
        default=None,
        metadata={
            "name": "ResponseType",
            "type": "Attribute",
        }
    )
