from __future__ import annotations

from dataclasses import dataclass

from travelport.models.base_air_exchange_quote_req import (
    BaseAirExchangeQuoteReq,
)

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class AirExchangeQuoteReq(BaseAirExchangeQuoteReq):
    """
    Request to quote the exchange of an itinerary.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"
