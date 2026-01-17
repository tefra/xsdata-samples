from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_air_exchange_multi_quote_req import (
    BaseAirExchangeMultiQuoteReq,
)

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirExchangeMultiQuoteReq(BaseAirExchangeMultiQuoteReq):
    """
    Request multiple quotes for the exchange of an itinerary. 1P
    transactions only.

    Parameters
    ----------
    type_value
        Type choices are "Detail" or "Summary"  Default will be Summary
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    type_value: str = field(
        default="Summary",
        metadata={
            "name": "Type",
            "type": "Attribute",
        },
    )
