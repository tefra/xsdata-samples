from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_search_rsp_1 import BaseSearchRsp1
from travelport.models.host_token_1 import HostToken1
from travelport.models.hotel_search_result import HotelSearchResult
from travelport.models.marketing_information_1 import MarketingInformation1
from travelport.models.type_hotel_reference_point import (
    TypeHotelReferencePoint,
)

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class BaseHotelSearchRsp(BaseSearchRsp1):
    """
    Base hotel Search Response.

    Parameters
    ----------
    reference_point
        Hotel reference point.  Applicable for 1G,1V,1P.
    hotel_search_result
    marketing_information
    host_token
    address_search_quality
        Indicates the address matching level success for hotel address or
        Postal Code searches. Valid values: "1"-"8". Providers 1G, 1V.
    """

    reference_point: None | TypeHotelReferencePoint = field(
        default=None,
        metadata={
            "name": "ReferencePoint",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
        },
    )
    hotel_search_result: list[HotelSearchResult] = field(
        default_factory=list,
        metadata={
            "name": "HotelSearchResult",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            "max_occurs": 999,
        },
    )
    marketing_information: None | MarketingInformation1 = field(
        default=None,
        metadata={
            "name": "MarketingInformation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    host_token: None | HostToken1 = field(
        default=None,
        metadata={
            "name": "HostToken",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    address_search_quality: None | int = field(
        default=None,
        metadata={
            "name": "AddressSearchQuality",
            "type": "Attribute",
        },
    )
