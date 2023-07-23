from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.air_itinerary_solution import AirItinerarySolution
from travelport.models.air_segment_list import AirSegmentList
from travelport.models.apisrequirements_list import ApisrequirementsList
from travelport.models.base_search_rsp_1 import BaseSearchRsp1
from travelport.models.fare_info_list import FareInfoList
from travelport.models.fare_remark_list import FareRemarkList
from travelport.models.flight_details_list import FlightDetailsList
from travelport.models.host_token_list_2 import HostTokenList2
from travelport.models.type_distance import TypeDistance

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class BaseAvailabilitySearchRsp(BaseSearchRsp1):
    """
    Availability Search response.
    """
    flight_details_list: None | FlightDetailsList = field(
        default=None,
        metadata={
            "name": "FlightDetailsList",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )
    air_segment_list: None | AirSegmentList = field(
        default=None,
        metadata={
            "name": "AirSegmentList",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )
    fare_info_list: None | FareInfoList = field(
        default=None,
        metadata={
            "name": "FareInfoList",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )
    fare_remark_list: None | FareRemarkList = field(
        default=None,
        metadata={
            "name": "FareRemarkList",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )
    air_itinerary_solution: list[AirItinerarySolution] = field(
        default_factory=list,
        metadata={
            "name": "AirItinerarySolution",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 999,
        }
    )
    host_token_list: None | HostTokenList2 = field(
        default=None,
        metadata={
            "name": "HostTokenList",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )
    apisrequirements_list: None | ApisrequirementsList = field(
        default=None,
        metadata={
            "name": "APISRequirementsList",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )
    distance_units: None | TypeDistance = field(
        default=None,
        metadata={
            "name": "DistanceUnits",
            "type": "Attribute",
        }
    )
