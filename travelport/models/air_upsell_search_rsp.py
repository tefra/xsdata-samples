from __future__ import annotations

from dataclasses import dataclass

from travelport.models.base_air_price_rsp import BaseAirPriceRsp

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirUpsellSearchRsp(BaseAirPriceRsp):
    """
    Response of Upsell Offers search for the given Itinerary.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"
