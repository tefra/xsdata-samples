from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.host_token_list_1 import HostTokenList1
from travelport.models.rail_fare_idlist import RailFareIdlist
from travelport.models.rail_fare_list import RailFareList
from travelport.models.rail_fare_note_list import RailFareNoteList
from travelport.models.rail_journey_list import RailJourneyList
from travelport.models.rail_pricing_solution import RailPricingSolution
from travelport.models.rail_segment_list import RailSegmentList
from travelport.models.type_response_type import TypeResponseType

__NAMESPACE__ = "http://www.travelport.com/schema/rail_v52_0"


@dataclass(kw_only=True)
class RailAvailabilitySearchRsp(BaseRsp1):
    """
    Returns the result of an availability search on host.

    Parameters
    ----------
    rail_segment_list
    rail_journey_list
    rail_pricing_solution
    rail_fare_note_list
    rail_fare_idlist
    rail_fare_list
    host_token_list
    response_type
        Indicates the type of information returned in
        RailShopAPIResponse(Schedules/Availability).
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    rail_segment_list: None | RailSegmentList = field(
        default=None,
        metadata={
            "name": "RailSegmentList",
            "type": "Element",
        },
    )
    rail_journey_list: None | RailJourneyList = field(
        default=None,
        metadata={
            "name": "RailJourneyList",
            "type": "Element",
        },
    )
    rail_pricing_solution: list[RailPricingSolution] = field(
        default_factory=list,
        metadata={
            "name": "RailPricingSolution",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    rail_fare_note_list: None | RailFareNoteList = field(
        default=None,
        metadata={
            "name": "RailFareNoteList",
            "type": "Element",
        },
    )
    rail_fare_idlist: None | RailFareIdlist = field(
        default=None,
        metadata={
            "name": "RailFareIDList",
            "type": "Element",
        },
    )
    rail_fare_list: None | RailFareList = field(
        default=None,
        metadata={
            "name": "RailFareList",
            "type": "Element",
        },
    )
    host_token_list: None | HostTokenList1 = field(
        default=None,
        metadata={
            "name": "HostTokenList",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    response_type: None | TypeResponseType = field(
        default=None,
        metadata={
            "name": "ResponseType",
            "type": "Attribute",
        },
    )
