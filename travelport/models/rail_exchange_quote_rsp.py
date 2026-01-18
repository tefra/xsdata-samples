from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.host_token_list_1 import HostTokenList1
from travelport.models.rail_exchange_solution import RailExchangeSolution
from travelport.models.rail_fare_idlist import RailFareIdlist
from travelport.models.rail_fare_list import RailFareList
from travelport.models.rail_fare_note_list import RailFareNoteList
from travelport.models.rail_journey_list import RailJourneyList
from travelport.models.rail_segment_list import RailSegmentList

__NAMESPACE__ = "http://www.travelport.com/schema/rail_v52_0"


@dataclass(kw_only=True)
class RailExchangeQuoteRsp(BaseRsp1):
    """
    Returns the result of an availability search on host.
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
    rail_exchange_solution: list[RailExchangeSolution] = field(
        default_factory=list,
        metadata={
            "name": "RailExchangeSolution",
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
