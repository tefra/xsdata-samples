from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_upsell_search_result import AirUpsellSearchResult
from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.hotel_upsell_search_result import (
    HotelUpsellSearchResult,
)
from travelport.models.vehicle_upsell_search_result import (
    VehicleUpsellSearchResult,
)

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass(kw_only=True)
class UpsellSearchRsp(BaseRsp1):
    """
    Response containing qualify and offer for the matching search criteria.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    air_upsell_search_result: list[AirUpsellSearchResult] = field(
        default_factory=list,
        metadata={
            "name": "AirUpsellSearchResult",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    hotel_upsell_search_result: list[HotelUpsellSearchResult] = field(
        default_factory=list,
        metadata={
            "name": "HotelUpsellSearchResult",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    vehicle_upsell_search_result: list[VehicleUpsellSearchResult] = field(
        default_factory=list,
        metadata={
            "name": "VehicleUpsellSearchResult",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    more_results: bool = field(
        metadata={
            "name": "MoreResults",
            "type": "Attribute",
            "required": True,
        }
    )
