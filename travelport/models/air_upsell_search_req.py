from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.air_base_req import AirBaseReq
from travelport.models.air_itinerary import AirItinerary
from travelport.models.air_price_result import AirPriceResult

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirUpsellSearchReq(AirBaseReq):
    """
    Request to search for Upsell Offers based on the Itinerary.

    Parameters
    ----------
    air_itinerary
        Provider: 1G,1V,1P,ACH-AirItinerary of the pricing request.
    air_price_result
        Provider: 1G,1V,1P,ACH-Result of AirPrice request. Upsell uses this
        to search for new offer.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_itinerary: None | AirItinerary = field(
        default=None,
        metadata={
            "name": "AirItinerary",
            "type": "Element",
            "required": True,
        },
    )
    air_price_result: list[AirPriceResult] = field(
        default_factory=list,
        metadata={
            "name": "AirPriceResult",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 16,
        },
    )
