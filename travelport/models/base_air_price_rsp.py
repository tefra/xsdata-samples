from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_itinerary import AirItinerary
from travelport.models.air_price_result import AirPriceResult
from travelport.models.base_rsp_1 import BaseRsp1

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class BaseAirPriceRsp(BaseRsp1):
    """
    Parameters
    ----------
    air_itinerary
        Provider: 1G,1V,1P,ACH.
    air_price_result
        Provider: 1G,1V,1P,ACH.
    """

    air_itinerary: None | AirItinerary = field(
        default=None,
        metadata={
            "name": "AirItinerary",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "required": True,
        },
    )
    air_price_result: list[AirPriceResult] = field(
        default_factory=list,
        metadata={
            "name": "AirPriceResult",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "min_occurs": 1,
            "max_occurs": 16,
        },
    )
